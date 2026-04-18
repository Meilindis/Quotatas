__version__ = "1.0.0"

import sys
import os
import random
from pathlib import Path
import shutil
import csv
from ast import literal_eval

# Pillow, a library for editing images. Needed to draw the quote texts on top of images.
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

# A file containing lists of words to be used in quotes, sorted by type
import word_collections

# A file containing the templates that define different quote structures
import template_collection

# Script that helps with putting text on images
from image_utils import ImageText

# Script that adds a button with a colour picker for the font colour
from colorbutton import ColorButton

# Generic Qt elements needed for the UI
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QPixmap, QImage, QColor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout, QFileDialog, QMessageBox, QComboBox, QGridLayout, QSpacerItem, QSizePolicy, QListWidget

# ---------------------------------------------------------------------------------------------------------------------------------------------
# RESOURCES

# Store current path for convenience
current_path = Path(__file__).parent.absolute()

# Helper function to check expression type
def evaluate(expression):
    try:
        return literal_eval(expression)
    except ValueError:
        return str(expression)
    except SyntaxError:
        return str(expression)

# Helper function to convert RGB colours to hex colours
def hexify(num):
    return f"{num:02x}"

def hexify_tuple(tup):
    return ''.join(hexify(value) for value in tup)

# ----------------------------------------------------------------------------------------------------------------------
# MAIN PROGRAM

if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # CREATE CONTAINERS TO STORE THE SELECTED QUOTES, IMAGES, AND FONTS

            # Store the quote here later:
            self.quote = ""
            self.image = []
            self.font = []
            self.full_history = [] # QUOTE - IMAGE - FONT
            self.selected_quote = 0
            self.font_collection = [] # FONT NAME - FONT SIZE
            self.image_collection = [] # IMAGE NAME - TEXT COLOUR (RGB) - ALIGNMENT - POSITION - X OFFSET - Y OFFSET            
            self.log = []
 
            self.log.append("Importing files...")
            # Import the files containing the words, fonts, and images that are used
            self.import_word_lists()
            self.import_font_collection()
            self.import_image_collection()

            # Create the UI components
            self.create_ui_components()
            # Create layouts to arrange the UI components
            self.arrange_layouts()
                        
            # Update the selected words based on the UI settings
            self.settings_changed()

        # -----------------------------------------------------------------------------------------------------------------------------
        # MEMBER FUNCTIONS

        def create_ui_components(self):
            self.setWindowTitle("Quotatas")
            my_icon = QIcon()
            my_icon.addFile(os.path.join(current_path, os.path.join('images','meilindis.png')))
            self.setWindowIcon(my_icon)
            self.log.append("Added window icon...")

            self.log.append("Setting up UI...")
            # CREATE UI COMPONENTS
            # Button to generate quotes
            self.button = QPushButton("Give me some wisdom!")
            self.button.setCheckable(True)
            self.button.clicked.connect(self.generate_quote)
            self.button.setStyleSheet('height: 100px; background-color: #b0cceb; color: black; text-align: center;')

            # Label that displays the generated quote image
            self.quote_area = QLabel()
            self.quote_area.setStyleSheet('background-color: black; color: white;')
            self.quote_area.resize(500, 500)            

            # Field that displays the generated quote in text only
            self.text_field = QTextEdit()
            self.text_field.setStyleSheet('background-color: #2e2e2e; color: #9e9e9e;')
            self.text_field.setReadOnly(True)

            # Back and forward buttons
            self.button_back = QPushButton("Previous")
            self.button_back.clicked.connect(self.previous_quote)
            self.button_back.setStyleSheet('background-color: orange; color:black;')

            self.button_forward = QPushButton("Next")
            self.button_forward.clicked.connect(self.next_quote)
            self.button_forward.setStyleSheet('background-color: orange; color:black;')

            # Saving and copying
            self.button_save = QPushButton("Save")
            self.button_save.clicked.connect(self.save_quote)
            self.button_save.setStyleSheet('background-color: #a3d3a7;')     

            # Settings toggles
            self.nsfw_toggle = QCheckBox(text="Include NSFW words")
            self.nsfw_toggle.stateChanged.connect(self.settings_changed)
            self.nsfw_toggle.setStyleSheet('background-color: #ffbcf1;')

            self.negative_toggle = QCheckBox(text="Include negative stuff (risky!)")
            self.negative_toggle.stateChanged.connect(self.settings_changed)
            self.negative_toggle.setStyleSheet('background-color: #ffe8a6;')            

            # Font settings - name
            self.change_font_label = QLabel("Change font:")
            self.change_font_label.setStyleSheet('border: 0px solid black;')
            self.change_font = QComboBox()
            self.change_font.currentTextChanged.connect(self.change_selected_font)
            self.change_font.setStyleSheet('background-color: #dfdfdf;')
            for font in self.font_collection:
                self.change_font.addItem(font[2])
            
            # Font settings - colour
            self.change_colour = ColorButton(color="#fff") 
            self.change_colour.colorChanged.connect(self.change_selected_colour)
            # Font settings - size
            self.change_font_size = QComboBox()
            self.change_font_size.currentTextChanged.connect(self.change_selected_font_size)
            self.change_font_size.setStyleSheet('background-color: #dfdfdf;')
            for i in (range(16, 42, 2)):
                self.change_font_size.addItem(str(i))
            
            # Export the created quotes so far (text only)
            self.button_export_quotes = QPushButton("Export session quotes")
            self.button_export_quotes.clicked.connect(self.export_quotes)
            self.button_export_quotes.setStyleSheet('background-color: orange; color:black;')

            # Export the log file
            self.button_export_log = QPushButton("Export log")
            self.button_export_log.clicked.connect(self.export_log)   
            self.button_export_log.setStyleSheet('background-color: #d8b6ec; color:black;')         

            self.log.append("Generated UI components...")
            
            self.log.append("Setting up splash screen...")
            # Set up the splash image with a different greeting every time the app is opened
            splash_image = os.path.join(current_path, os.path.join('images','bot.png'))
            self.image = [splash_image, (255, 255, 255), 'center', 'bottom', 0, 0]
            self.font = random.choice(self.font_collection)
            self.font[1] = 34
            self.quote = random.choice(word_collections.greetings)
            self.update_ui_elements()
            self.create_quote_image()
            pixmap = QPixmap('temp.png')
            self.quote_area.resize(pixmap.width(), pixmap.height())
            self.quote_area.setPixmap(pixmap)

        def arrange_layouts(self):
            self.log.append("Setting up UI layout...")
            # Arrange the back/forward buttons horizontally
            layoutH = QHBoxLayout()
            layoutH.addWidget(self.button_back)
            layoutH.addWidget(self.button_save)
            layoutH.addWidget(self.button_forward)
            nav_container = QWidget()
            nav_container.setLayout(layoutH)

            # Line out the settings in a grid
            settingsLayout = QHBoxLayout()
            settingsLayout.addWidget(self.change_font_label)
            settingsLayout.addWidget(self.change_font)
            settingsLayout.addWidget(self.change_colour)
            settingsLayout.addWidget(self.change_font_size)
            settingsContainer = QWidget()
            settingsContainer.setStyleSheet('background-color: #b1b1b1')
            settingsContainer.setLayout(settingsLayout)

            # Arrange all settings elements in a grid
            layoutGrid = QGridLayout()       
            layoutGrid.addWidget(self.negative_toggle, 0, 0)
            layoutGrid.addWidget(self.nsfw_toggle, 1, 0) 
            layoutGrid.addWidget(self.button_export_log, 1, 1)
            layoutGrid.addWidget(self.button_export_quotes, 0, 1)      

            vert_container = QWidget()
            vert_container.setLayout(layoutGrid)

            # Add quotes and navigation to their own container
            quoteLayout = QVBoxLayout()
            quoteLayout.addWidget(settingsContainer)  
            quoteLayout.addWidget(self.quote_area)
            quoteLayout.addWidget(nav_container)
            quoteLayout.addWidget(self.button)

            quote_container = QWidget()
            quote_container.setLayout(quoteLayout)

            # Combine everything into one layout
            layoutApp = QVBoxLayout()
            layoutApp.addWidget(vert_container)
            layoutApp.addWidget(quote_container)

            # Add the layout to an overall widget and add to main window
            container = QWidget()
            container.setStyleSheet('background-color: #808080; color:black; border: 2px solid black; font-size: 20px; padding: 4px;')
            container.setLayout(layoutApp)

            self.setCentralWidget(container) 
            self.log.append("UI up and running!")

        # Read font info from file
        def import_font_collection(self):
            self.log.append("Importing font collection...")
            font_location = os.path.join(current_path, 'resources', 'font_collection.csv')
            with open(font_location, newline='') as csvfile:
                fontreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                parsed = (list(evaluate(field) for field in row) for row in fontreader)
                for row in parsed:
                    self.font_collection.append(row)
            self.log.append("Font collection imported!")

         # Read image info from file
        def import_image_collection(self):
            self.log.append("Importing image collection...")
            image_location = os.path.join(current_path, 'resources', 'image_collection.csv')
            with open(image_location, newline='') as csvfile:
                imagereader = csv.reader(csvfile, delimiter=';', quotechar='|')
                parsed = (list(evaluate(field) for field in row) for row in imagereader)
                for row in parsed:
                    self.image_collection.append(row)
            self.log.append("Image collection imported!")

        # Define what happens when the button is pressed
        def generate_quote(self):
            self.log.append("Generating quote...")
            self.text_field.setText("")
            # Set the selected quote to the last one (in case the user was looking at an earlier quote)
            if len(self.full_history) > 1:
                self.selected_quote = len(self.full_history) - 1
            # Adding new quote, so exporting makes sense again
            self.button_export_quotes.setText("Export session quotes")
            # Select the random parameters
            self.create_basics()
            self.update_ui_elements()
            # Create the image
            self.create_quote_image()
            
        def create_basics(self):
        	# Select the random parameters of the quote
            self.log.append("Selecting image...")
            self.image = random.choice(self.image_collection)
            self.log.append("Image selected!")
            self.log.append("Selecting font...")
            self.font = random.choice(self.font_collection)
            self.log.append("Font selected!")
            self.log.append("Generating quote text...")
            self.quote = random.choice(template_collection.template_list)()
            self.log.append("Quote text generated!")

            # Add and set the selected parameters to the list of 
            self.log.append("Adding quote to history...")
            self.full_history.append([self.quote, self.image, self.font])
            self.selected_quote = len(self.full_history) - 1

        def update_ui_elements(self):      
            # Update other variables and UI elements 
            self.log.append("Updating the font colour...")                 
            self.change_colour.setColor('#' + hexify_tuple(self.image[1]))
            self.log.append("Updated font colour to RGB" + str(self.image[1]) + ".")
            index_font = self.change_font.findText(self.font[2])
            if index_font >= 0:
                self.log.append("Updating the font selector...")
                self.change_font.setCurrentIndex(index_font)
                self.change_font_size.setCurrentIndex(self.change_font_size.findText(str(self.font[1])))
                self.log.append("Font selected.")

        def create_quote_image(self):
            # Can't create an image without parameters
            if self.image == [] or self.font == [] or self.selected_quote == -1:
                self.log.append("Error. Could not generate quote, insufficient paramenters.")
                return

            # Prepare the image
            self.log.append("Drawing text on image...")
            current_dir = Path(__file__).parent.absolute()            
            image_path = os.path.join(current_dir, 'images', self.image[0])
            image = Image.open(image_path)

            color = self.image[1]
            location = self.image[2]

            text = self.quote
            font_name = os.path.join(current_dir, 'fonts', self.font[0])
            font_custom_size = self.font[1]
            line_height = font_custom_size + 8
            img = ImageText(image, background=(255, 255, 255, 200)) # 200 = alpha
            
            # Determine number of lines
            nr_of_lines = text.count("\n") + 1
            # Add the separate lines to a list
            lines = text.splitlines()
            x_val = 20 # default indentation
            y_val = 0

            if self.image[3] == 'top':
                x_val += self.image[4]
                y_val = 30 + self.image[5]                
            elif self.image[3] == 'middle':
                x_val += self.image[4]
                y_val = 225 + self.image[5]
                # Make sure the text is centered around the given y value
                y_val -= (nr_of_lines * 35)/2
            elif self.image[3] == 'bottom':
                x_val += self.image[4]
                y_val = 450 + self.image[5]
                # Make sure the text starts high enough
                y_val -= (nr_of_lines * 35)
            else:
                return
            # Assign the resulting offset to x/y
            x = x_val
            y = y_val

            # Now draw each line onto the image
            for line in lines:
                img.write_text_box((x, y), line, box_width=180, font_filename=font_name,
                        font_size=font_custom_size, color=color, place=location)
                y += line_height

            # Save in temporary location
            img.save('temp.png')

            # Display the modified image
            pixmap = QPixmap('temp.png')
            self.quote_area.resize(pixmap.width(), pixmap.height())
            self.quote_area.setPixmap(pixmap)

        def change_selected_font(self):
            # A new font has been selected, so pick up the selected item's text
            new_font = self.change_font.currentText()
            # If somehow no font is selected
            if new_font == "":
                return
            # Find this font in the collection
            for font in self.font_collection:
                if font[2] == new_font:
                    self.font = font
            # Re-create the image with the new font setting
            self.create_quote_image()

        def change_selected_font_size(self):
            if self.font != []:
                new_size = self.change_font_size.currentText()
                if new_size == "":
                    return
                self.font[1] = int(new_size)
                self.create_quote_image()

        def change_selected_colour(self):
            # A new colour has been selected, so get the new colour name and save it
            if self.image != None:
                # Convert to RGB and store 
                self.image[1] = ImageColor.getcolor(self.change_colour.color(), "RGB")
                # Re-create the image
                self.create_quote_image()

        def save_quote(self):
            # Check if there's a generated image present
            try:
                if os.path.isfile('temp.png'):
                    # Create a dialog in which to select a name and location
                    self.save_dialog = QFileDialog()
                    save_file_name = self.save_dialog.getSaveFileName(self, 'Save quote', '', filter='Image files (.png)', selectedFilter='*.png')
                    save_file = save_file_name[0] + '.png'
                    # Check if the filename already exists
                    if os.path.isfile(save_file):
                        dlg = QMessageBox(self)
                        dlg.setStyleSheet('background-color: #b1b1b1; border:1px solid black;')
                        dlg.setWindowTitle("File exists")
                        dlg.setText("The selected filename is already in use. Save anyway?")
                        dlg.setStandardButtons(
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
                        )
                        dlg.setIcon(QMessageBox.Icon.Question)
                        selected = dlg.exec()

                        if selected == QMessageBox.StandardButton.Yes:
                            shutil.copyfile('temp.png', save_file)
                        else:
                            pass                    
                    else:
                        shutil.copyfile('temp.png', save_file)
            # If no generated image is present, there's nothing to save
                else:
                    self.text_field.setText("No image available to save.")
            except FileNotFoundError:
                self.text_field.setText("No image available to save.")

        # What happens when the "Previous" button is clicked
        def previous_quote(self):
            # If there's more than one quote and you're not looking at the first quote, you can go back
            if len(self.full_history) > 1 and self.selected_quote >= 1:
                self.selected_quote = self.selected_quote - 1
                self.quote = self.full_history[self.selected_quote][0]
                self.image = self.full_history[self.selected_quote][1]
                self.font = self.full_history[self.selected_quote][2]
                self.change_colour.setColor('#' + hexify_tuple(self.image[1]))
                
                self.create_quote_image()
            else:
                return

        # What happens when the "Next" button is clicked
        def next_quote(self):
            # If you are not looking at the most recent quote, you can go forward
            if self.selected_quote < len(self.full_history) - 1:
                self.selected_quote = self.selected_quote + 1
                self.quote = self.full_history[self.selected_quote][0]
                self.image = self.full_history[self.selected_quote][1]
                self.font = self.full_history[self.selected_quote][2]
                self.change_colour.setColor('#' + hexify_tuple(self.image[1]))

                self.create_quote_image()
            else:
                return

        # Export the quote history to a txt file in the current directory - will overwrite without warning!
        def export_quotes(self):
            with open('dutch_wisdom_quote_collection.txt', 'w') as f:
                for quote in self.full_history:
                    f.write(f"{quote[0]}\n\n---\n\n")

            self.button_export_quotes.setText("Exported!")

        # Export the log to log.txt (will overwrite without warning)
        def export_log(self):
            with open('log.txt', 'w') as f:
                for line in self.log:
                    f.write(f"{line}\n")

        # Determine the available word collection depending on the toggles (NSFW/negative on or off)
        def settings_changed(self):
            # Set all word collections to neutral
            word_collections.nouns_singular = word_collections.nouns_singular_sfw + word_collections.people_singular + word_collections.animals_singular + word_collections.verbs_active_sfw + word_collections.food_singular
            word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.nouns_plural_sfw + word_collections.food_plural
            word_collections.adjectives = word_collections.adjectives_positive + word_collections.adjectives_neutral + word_collections.colours
            word_collections.verbs = word_collections.verbs_sfw
            word_collections.verbs_third_person = word_collections.verbs_third_person_sfw
            word_collections.verbs_ing = word_collections.verbs_ing_sfw
            word_collections.verbs_intransitive = word_collections.verbs_intransitive_sfw
            word_collections.concepts = word_collections.concepts_neutral + word_collections.concepts_positive + word_collections.food_concepts
            word_collections.comparatives = word_collections.comparatives_sfw
            word_collections.superlatives = word_collections.superlatives_sfw
            word_collections.situations = word_collections.situations_sfw
            word_collections.situations_active = word_collections.situations_active_sfw
            word_collections.people_singular = word_collections.people_singular_sfw
            word_collections.people_plural = word_collections.people_plural_sfw
            word_collections.cliches = word_collections.cliches_sfw
            # Add NSFW
            if self.nsfw_toggle.isChecked():
                word_collections.nouns_singular = word_collections.nouns_singular + word_collections.nouns_singular_nsfw + word_collections.animals_singular + word_collections.verbs_active_sfw + word_collections.verbs_active_nsfw
                word_collections.nouns_plural = word_collections.nouns_plural + word_collections.nouns_plural_nsfw
                word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_nsfw
                word_collections.verbs = word_collections.verbs + word_collections.verbs_nsfw
                word_collections.verbs_third_person = word_collections.verbs_third_person + word_collections.verbs_third_person_nsfw
                word_collections.verbs_ing = word_collections.verbs_ing + word_collections.verbs_ing_nsfw
                word_collections.verbs_intransitive = word_collections.verbs_intransitive_sfw + word_collections.verbs_intransitive_nsfw
                word_collections.concepts = word_collections.concepts + word_collections.concepts_nsfw
                word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_nsfw
                word_collections.comparatives = word_collections.comparatives + word_collections.comparatives_nsfw
                word_collections.superlatives = word_collections.superlatives + word_collections.superlatives_nsfw
                word_collections.situations = word_collections.situations + word_collections.situations_nsfw
                word_collections.situations_active = word_collections.situations_active + word_collections.situations_active_nsfw
                word_collections.cliches = word_collections.cliches + word_collections.cliches_nsfw
            # Add negative stuff
            if self.negative_toggle.isChecked() == True:
                word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_negative
                word_collections.concepts = word_collections.concepts + word_collections.concepts_negative
                word_collections.people_singular = word_collections.people_singular + word_collections.people_singular_neg
                word_collections.people_plural = word_collections.people_plural + word_collections.people_plural_neg
            # Remove anything but positive
            if self.negative_toggle.isChecked() == False:
                word_collections.adjectives = word_collections.adjectives_positive               
        
        # Import the word collection from the files in the folder word_collections
        def import_word_lists(self):
            word_collections.adjectives_positive = word_collections.import_list("adjectives_positive.txt")
            word_collections.adjectives_negative = word_collections.import_list("adjectives_negative.txt")
            word_collections.adjectives_neutral = word_collections.import_list("adjectives_neutral.txt")
            word_collections.colours = word_collections.import_list("colours.txt")
            word_collections.nouns_singular_sfw = word_collections.import_list("nouns_singular_sfw.txt")
            word_collections.nouns_plural_sfw = word_collections.import_list("nouns_plural_sfw.txt")
            word_collections.people_singular_sfw = word_collections.import_list("people_singular_sfw.txt")
            word_collections.people_plural_sfw = word_collections.import_list("people_plural_sfw.txt")
            word_collections.animals_singular = word_collections.import_list("animals_singular.txt")
            word_collections.animals_plural = word_collections.import_list("animals_plural.txt")
            word_collections.food_singular = word_collections.import_list("food_singular.txt")
            word_collections.food_plural = word_collections.import_list("food_plural.txt")
            word_collections.verbs_sfw = word_collections.import_list("verbs_sfw.txt")
            word_collections.verbs_intransitive_sfw = word_collections.import_list("verbs_intransitive_sfw.txt")
            word_collections.verbs_third_person_sfw = word_collections.import_list("verbs_third_person_sfw.txt")
            word_collections.verbs_active_sfw = word_collections.import_list("verbs_active_sfw.txt")
            word_collections.verbs_ing_sfw = word_collections.import_list("verbs_ing_sfw.txt")
            word_collections.verbs_mandatory_sfw = word_collections.import_list("verbs_mandatory_sfw.txt")
            word_collections.times = word_collections.import_list("times.txt")
            word_collections.audiences = word_collections.import_list("audiences.txt")
            word_collections.adverbs = word_collections.import_list("adverbs.txt")
            word_collections.concepts_positive = word_collections.import_list("concepts_positive.txt")
            word_collections.concepts_neutral = word_collections.import_list("concepts_neutral.txt")
            word_collections.concepts_negative = word_collections.import_list("concepts_negative.txt")
            word_collections.concepts_nsfw = word_collections.import_list("concepts_nsfw.txt")
            word_collections.verbs_active_sfw = word_collections.import_list("verbs_active_sfw.txt")
            word_collections.nouns_singular_nsfw = word_collections.import_list("nouns_singular_nsfw.txt")
            word_collections.nouns_plural_nsfw = word_collections.import_list("nouns_plural_nsfw.txt")
            word_collections.adjectives_nsfw = word_collections.import_list("adjectives_nsfw.txt")
            word_collections.verbs_nsfw = word_collections.import_list("verbs_nsfw.txt")
            word_collections.verbs_intransitive_nsfw = word_collections.import_list("verbs_intransitive_nsfw.txt")
            word_collections.verbs_third_person_nsfw = word_collections.import_list("verbs_third_person_nsfw.txt")
            word_collections.verbs_active_nsfw = word_collections.import_list("verbs_active_nsfw.txt")
            word_collections.verbs_ing_nsfw = word_collections.import_list("verbs_ing_nsfw.txt")
            word_collections.comparatives_sfw = word_collections.import_list("comparatives_sfw.txt")
            word_collections.comparatives_nsfw = word_collections.import_list("comparatives_nsfw.txt")
            word_collections.superlatives_sfw = word_collections.import_list("superlatives_sfw.txt")
            word_collections.superlatives_nsfw = word_collections.import_list("superlatives_nsfw.txt")
            word_collections.situations_sfw = word_collections.import_list("situations_sfw.txt")
            word_collections.situations_nsfw = word_collections.import_list("situations_nsfw.txt")
            word_collections.situations_active_sfw = word_collections.import_list("situations_active_sfw.txt")
            word_collections.situations_active_nsfw = word_collections.import_list("situations_active_nsfw.txt")
            word_collections.prepositions = word_collections.import_list("prepositions.txt")
            word_collections.people_singular_neg = word_collections.import_list("people_singular_neg.txt")
            word_collections.people_plural_neg = word_collections.import_list("people_plural_neg.txt")
            word_collections.zodiac = word_collections.import_list("zodiac.txt")
            word_collections.sometimes = word_collections.import_list("sometimes.txt")
            word_collections.cliches_sfw = word_collections.import_list("cliches_sfw.txt")
            word_collections.cliches_nsfw = word_collections.import_list("cliches_nsfw.txt")
            word_collections.food_concepts = word_collections.import_list("food_concepts.txt")

        # Export every word list and make sure the words are in alphabetical order.
        # This function is not used by default and is only there as a convenience.
        def export_word_lists(self):
            word_collections.export_list(word_collections.adjectives_positive, "adjectives_positive")
            word_collections.export_list(word_collections.adjectives_negative, "adjectives_negative")
            word_collections.export_list(word_collections.adjectives_neutral, "adjectives_neutral")
            word_collections.export_list(word_collections.colours, "colours")
            word_collections.export_list(word_collections.nouns_singular_sfw, "nouns_singular_sfw")
            word_collections.export_list(word_collections.nouns_plural_sfw, "nouns_plural_sfw")
            word_collections.export_list(word_collections.people_singular_sfw, "people_singular_sfw")
            word_collections.export_list(word_collections.people_plural_sfw, "people_plural_sfw")
            word_collections.export_list(word_collections.animals_singular, "animals_singular")
            word_collections.export_list(word_collections.animals_plural, "animals_plural")
            word_collections.export_list(word_collections.food_singular, "food_singular")
            word_collections.export_list(word_collections.food_plural, "food_plural")
            word_collections.export_list(word_collections.verbs_sfw, "verbs_sfw")
            word_collections.export_list(word_collections.verbs_intransitive_sfw, "verbs_intransitive_sfw")
            word_collections.export_list(word_collections.verbs_third_person_sfw, "verbs_third_person_sfw")
            word_collections.export_list(word_collections.verbs_active_sfw, "verbs_active_sfw")
            word_collections.export_list(word_collections.verbs_ing_sfw, "verbs_ing_sfw")
            word_collections.export_list(word_collections.verbs_mandatory_sfw, "verbs_mandatory_sfw")
            word_collections.export_list(word_collections.times, "times")
            word_collections.export_list(word_collections.audiences, "audiences")
            word_collections.export_list(word_collections.adverbs, "adverbs")
            word_collections.export_list(word_collections.concepts_positive, "concepts_positive")
            word_collections.export_list(word_collections.concepts_neutral, "concepts_neutral")
            word_collections.export_list(word_collections.concepts_negative, "concepts_negative")
            word_collections.export_list(word_collections.concepts_nsfw, "concepts_nsfw")
            word_collections.export_list(word_collections.verbs_active_sfw, "verbs_active_sfw")
            word_collections.export_list(word_collections.nouns_singular_nsfw, "nouns_singular_nsfw")
            word_collections.export_list(word_collections.nouns_plural_nsfw, "nouns_plural_nsfw")
            word_collections.export_list(word_collections.adjectives_nsfw, "adjectives_nsfw")
            word_collections.export_list(word_collections.verbs_nsfw, "verbs_nsfw")
            word_collections.export_list(word_collections.verbs_intransitive_nsfw, "verbs_intransitive_nsfw")
            word_collections.export_list(word_collections.verbs_third_person_nsfw, "verbs_third_person_nsfw")
            word_collections.export_list(word_collections.verbs_active_nsfw, "verbs_active_nsfw")
            word_collections.export_list(word_collections.verbs_ing_nsfw, "verbs_ing_nsfw")
            word_collections.export_list(word_collections.comparatives_sfw, "comparatives_sfw")
            word_collections.export_list(word_collections.comparatives_nsfw, "comparatives_nsfw")
            word_collections.export_list(word_collections.superlatives_sfw, "superlatives_sfw")
            word_collections.export_list(word_collections.superlatives_nsfw, "superlatives_nsfw")
            word_collections.export_list(word_collections.situations_sfw, "situations_sfw")
            word_collections.export_list(word_collections.situations_nsfw, "situations_nsfw")
            word_collections.export_list(word_collections.situations_active_sfw, "situations_active_sfw")
            word_collections.export_list(word_collections.situations_active_nsfw, "situations_active_nsfw")
            word_collections.export_list(word_collections.prepositions, "prepositions")
            word_collections.export_list(word_collections.people_singular_neg, "people_singular_neg")
            word_collections.export_list(word_collections.people_plural_neg, "people_plural_neg")
            word_collections.export_list(word_collections.zodiac, "zodiac")
            word_collections.export_list(word_collections.sometimes, "sometimes")
            word_collections.export_list(word_collections.cliches_sfw, "cliches_sfw")
            word_collections.export_list(word_collections.cliches_nsfw, "cliches_nsfw")
            word_collections.export_list(word_collections.food_concepts, "food_concepts.txt")

        def export_font_collection(self):
            font_location = os.path.join(current_path, 'resources')
            font_location = os.path.join(font_location, 'font_collection.csv')
            with open(font_location, 'w', newline='') as csvfile:
                fontwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for line in self.font_collection:
                    fontwriter.writerow(line)

        def export_image_collection(self):
            image_location = os.path.join(current_path, 'resources')
            image_location = os.path.join(image_location, 'image_collection.csv')
            with open(image_location, 'w', newline='') as csvfile:
                imagewriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for line in self.image_collection:
                    imagewriter.writerow(line)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
