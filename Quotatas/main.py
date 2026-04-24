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

# Logging
import logging

# Dark/light theme (mostly to fix it in Windows)
import qdarktheme

# Script that adds a button with a colour picker for the font colour
from colorbutton import ColorButton

# Generic Qt elements needed for the UI
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QPixmap, QImage, QColor, QIcon, QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout, QFileDialog, QMessageBox, QComboBox, QGridLayout, QSpacerItem, QSizePolicy, QListWidget, QStatusBar, QToolBar

# ---------------------------------------------------------------------------------------------------------------------------------------------
# RESOURCES

# Store current path for convenience
current_path = Path(__file__).parent.absolute()
icon_path = os.path.join(current_path, 'icons')
logger = logging.getLogger(__name__)

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # CREATE CONTAINERS TO STORE THE SELECTED QUOTES, IMAGES, AND FONTS

        # Store the quote here later:
        self._quote = ""
        self._image = []
        self._font = []
        self._full_history = [] # QUOTE - IMAGE - FONT
        self._selected_quote = 0
        self._font_collection = [] # FONT NAME - FONT SIZE
        self._image_collection = [] # IMAGE NAME - TEXT COLOUR (RGB) - ALIGNMENT - POSITION - X OFFSET - Y OFFSET            
        self._generating_quote = False # Whether a quote is being actively generated.

        logger.info("Importing files...")

        # Import the files containing the words, fonts, and images that are used
        self.import_word_lists()
        self.import_font_collection()
        self.import_image_collection()

        # Create the UI components
        logger.info("Creating UI components...")
        self.create_ui_components()

        # Set up splash screen
        logger.info("Creating splash screen...")
        self.generate_splash_screen()
        
        # Create layouts to arrange the UI components
        logger.info("Setting up UI layout...")
        self.arrange_layouts()
        self.add_toolbar()
        
        # Import the previous settings (if they exist)
        logger.info("Importing settings...")
        self.import_settings()

        # Update the selected words based on the UI settings
        logger.info("Updating word collections...")
        self.settings_changed()

        logger.info("UI is up and running. Ready to start generating quotes!\n------------------------")
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # MEMBER FUNCTIONS

    def create_ui_components(self):
        self.setWindowTitle("Quotatas")
        my_icon = QIcon()
        my_icon.addFile(os.path.join(current_path, os.path.join('icons','quotatas-teal.ico')))
        self.setWindowIcon(my_icon)
        logger.info("\tAdded window icon.")

        # CREATE UI COMPONENTS
        logger.info("\tGenerating components...")
        # Button to generate quotes
        self.button_generate_quote = QPushButton(QIcon(os.path.join(icon_path, 'quotatas.ico')),"Give me some wisdom!")
        self.button_generate_quote.setIconSize(QSize(32, 32))
        self.button_generate_quote.setCheckable(True)
        self.button_generate_quote.clicked.connect(self.generate_quote)
        self.button_generate_quote.setMinimumHeight(120)
        self.button_generate_quote.setObjectName('button_generate_quote')
        self.button_generate_quote.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_generate_quote.setIconSize(QSize(32, 32))

        # Label that displays the generated quote image
        self.quote_area = QLabel()
        self.quote_area.resize(500, 500)  
        self.quote_area.setObjectName('quote_area')   
        self.quote_area.setStyleSheet('background-color: #2a4648;')       

        # Font settings - name
        self.change_font_label = QLabel("Change font:")
        self.change_font_label.setObjectName('change_font_label')
        self.change_font = QComboBox()
        self.change_font.setObjectName('change_font')
        self.change_font.currentTextChanged.connect(self.change_selected_font)
        # Temporarily add empty item until first font name is selected 
        self.change_font.addItem("")
        self.change_font.setCurrentIndex(self.change_font.findText(""))
        # Add the font names
        for font in self._font_collection:
            self.change_font.addItem(font[2])
        
        # Font settings - colour
        self.change_colour = ColorButton(color="#fff") 
        self.change_colour.setObjectName('set_colour')
        self.change_colour.colorChanged.connect(self.change_selected_colour)
        # Font settings - size
        self.change_font_size = QComboBox()
        self.change_font_size.setObjectName('change_font_size')
        self.change_font_size.currentTextChanged.connect(self.change_selected_font_size)
        # Temporarily add empty item until first font size is selected
        self.change_font_size.addItem("")
        self.change_font_size.setCurrentIndex(self.change_font_size.findText(""))
        # Add the font sizes
        for i in (range(16, 42, 2)):
            self.change_font_size.addItem(str(i))
        
        logger.info("UI components created.")

    def generate_splash_screen(self):
        # Set up the splash image with a different greeting every time the app is opened
        splash_image = os.path.join(current_path, os.path.join('images','quotatas-500px-inverted.png'))
        self._image = [splash_image, (255, 255, 255), 'justify', 'bottom', 0, 20]
        self._font = random.choice(self._font_collection)
        # Store original font size because the reference is updated
        font_size = self._font[1]
        self._font[1] = 34
        self._quote = random.choice(word_collections.greetings)
        self.update_ui_elements()
        self.create_quote_image()
        # Restore the original font size of the font
        self._font[1] = font_size
        pixmap = QPixmap('temp.png')
        self.quote_area.resize(pixmap.width(), pixmap.height())
        self.quote_area.setPixmap(pixmap)
        logger.info("Splash screen created.")
        
        # Remove empty entries that are now redundant
        self.change_font.removeItem(self.change_font.findText(""))
        self.change_font_size.removeItem(self.change_font_size.findText(""))

    def arrange_layouts(self):
        logger.info("Setting up UI layout...")

        # Line out the settings in a grid
        self.font_settings_layout = QHBoxLayout()
        self.font_settings_layout.addWidget(self.change_font_label)
        self.font_settings_layout.addWidget(self.change_font)
        self.font_settings_layout.addWidget(self.change_colour)
        self.font_settings_layout.addWidget(self.change_font_size)
        self.font_settings_container = QWidget()
        self.font_settings_container.setObjectName('font_settings_container')
        self.font_settings_container.setLayout(self.font_settings_layout)

        # Add quotes and navigation to their own container
        self.quote_area_layout = QVBoxLayout()
        self.quote_area_layout.addWidget(self.quote_area)
        self.quote_area_layout.addWidget(self.font_settings_container)  
        self.quote_area_layout.addWidget(self.button_generate_quote)

        self.quote_area_container = QWidget()
        self.quote_area_container.setObjectName('quote_area_container')
        self.quote_area_container.setLayout(self.quote_area_layout)

        # Combine everything into one layout
        self.app_layout = QVBoxLayout()
        self.app_layout.addWidget(self.quote_area_container)

        # Add the layout to an overall widget and add to main window
        self.app_container = QWidget()
        self.app_container.setObjectName('app_container')
        self.app_container.setLayout(self.app_layout)

        self.setCentralWidget(self.app_container) 
        logger.info("Layout arranged.")

    def add_toolbar(self):
        logger.info("Adding toolbar...")
        self.toolbar = QToolBar("Toolbar")
        self.toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(self.toolbar)

        self.button_nsfw_action = QAction(QIcon(os.path.join(icon_path, 'nsfw.ico')), "Include NSFW words", self)
        self.button_nsfw_action.setStatusTip("Include NSFW words")
        self.button_nsfw_action.triggered.connect(self.settings_changed)
        self.button_nsfw_action.setCheckable(True)
        self.toolbar.addAction(self.button_nsfw_action)

        self.button_negative_action = QAction(QIcon(os.path.join(icon_path, 'negative.ico')), "Include negative words (tricky!)", self)
        self.button_negative_action.setStatusTip("Include negative words (tricky!)")
        self.button_negative_action.triggered.connect(self.settings_changed)
        self.button_negative_action.setCheckable(True)
        self.toolbar.addAction(self.button_negative_action)

        self.toolbar.addSeparator()

        self.button_generate_action = QAction(QIcon(os.path.join(icon_path, 'quotatas-teal.ico')), "Generate quote", self)
        self.button_generate_action.setStatusTip("Generate a new quote image")
        self.button_generate_action.triggered.connect(self.generate_quote)
        self.toolbar.addAction(self.button_generate_action)

        self.button_previous_action = QAction(QIcon(os.path.join(icon_path, 'previous.ico')), "Go back to the previous quote", self)
        self.button_previous_action.setStatusTip("Go back to the previous quote")
        self.button_previous_action.triggered.connect(self.previous_quote)
        self.toolbar.addAction(self.button_previous_action)
        self.button_previous_action.setEnabled(False) # no previous quote yet

        self.label_position = QLabel("0/0")
        self.label_position.setStatusTip("The quote index within your current quote collection")
        self.toolbar.addWidget(self.label_position)

        self.button_next_action = QAction(QIcon(os.path.join(icon_path, 'next.ico')), "Go to the next quote", self)
        self.button_next_action.setStatusTip("Go to the next quote")
        self.button_next_action.triggered.connect(self.next_quote)
        self.toolbar.addAction(self.button_next_action)
        self.button_next_action.setEnabled(False) # no next quote yet

        self.button_save_quote_action = QAction(QIcon(os.path.join(icon_path, 'save.ico')), "Save quote", self)
        self.button_save_quote_action.setStatusTip("Save the current quote image")
        self.button_save_quote_action.triggered.connect(self.save_quote)
        self.toolbar.addAction(self.button_save_quote_action)
        self.button_save_quote_action.setEnabled(False) # no image to save yet

        self.toolbar.addSeparator()

        self.button_export_quotes_action = QAction(QIcon(os.path.join(icon_path, 'export-quotes.ico')), "Export the quotes so far (text only)", self)
        self.button_export_quotes_action.setStatusTip("Export the quotes so far (text only)")
        self.button_export_quotes_action.triggered.connect(self.export_quotes)
        self.toolbar.addAction(self.button_export_quotes_action)
        self.button_export_quotes_action.setEnabled(False) # nothing to export yet

        self.toolbar.addSeparator()

        self.label_theme = QLabel("Theme: ")
        self.toolbar.addWidget(self.label_theme)

        self.combo_theme = QComboBox()
        self.combo_theme.setStatusTip("Change the UI theme (dark/light)")
        self.combo_theme.addItems(qdarktheme.get_themes())
        self.combo_theme.setCurrentIndex(self.combo_theme.findText("dark"))
        self.combo_theme.currentTextChanged.connect(qdarktheme.setup_theme)
        self.combo_theme.currentTextChanged.connect(self.update_stylesheet)
        self.toolbar.addWidget(self.combo_theme)

        #self.setStatusBar(QStatusBar(self))
        logger.info("Toolbar added.")

    def update_stylesheet(self):
        qdarktheme.setup_theme(self.combo_theme.currentText(), custom_colors={"primary": "#2b8d94"}, additional_qss=qss)

    # Read font info from file
    def import_font_collection(self):
        logger.info("\tImporting font collection...")
        font_location = os.path.join(current_path, 'resources', 'font_collection.csv')
        if os.path.isfile(font_location):
            with open(font_location, newline='') as csvfile:
                fontreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                parsed = (list(evaluate(field) for field in row) for row in fontreader)
                for row in parsed:
                    self._font_collection.append(row)
            logger.info("\tFont collection imported.")
        else:
            logger.info("Font collection file not found.")

        # Read image info from file
    def import_image_collection(self):
        logger.info("\tImporting image collection...")
        image_location = os.path.join(current_path, 'resources', 'image_collection.csv')
        if os.path.isfile(image_location):
            with open(image_location, newline='') as csvfile:
                imagereader = csv.reader(csvfile, delimiter=';', quotechar='|')
                parsed = (list(evaluate(field) for field in row) for row in imagereader)
                for row in parsed:
                    self._image_collection.append(row)
            logger.info("\tImage collection imported.")
        else:
            logger.info("Image collection file not found.")

    # Define what happens when the button is pressed
    def generate_quote(self):
        logger.info("Generating quote...")
        # Set the selected quote to the last one (in case the user was looking at an earlier quote)
        if len(self._full_history) > 1:
            self._selected_quote = len(self._full_history) - 1
        # Select the random parameters
        logger.info("Setting basic paramenters and updating UI...")
        self.create_basics()
        self._generating_quote = True
        self.update_ui_elements()
        # Create the image
        logger.info("Creating quote image...")
        self.create_quote_image()
        self._generating_quote = False
        self.update_quote_counter()
        # Enable/disable buttons depending on context
        self.update_toolbar_buttons()
        logger.info("New quote image created.")
        
    def create_basics(self):
        # Select the random parameters of the quote
        logger.info("\tSelecting image...")
        self._image = random.choice(self._image_collection)
        logger.info("\tImage selected: " + self._image[0] + ".")
        logger.info("\tSelecting font...")
        self._font = random.choice(self._font_collection)
        logger.info("\tFont selected: " + self._font[2] + ".")
        logger.info("\tGenerating quote text...")
        self._quote = random.choice(template_collection.template_list)()
        logger.info("\tQuote text generated:\n\n " + self._quote + "\n\n")

        # Add and set the selected parameters to the list of quotes
        logger.info("\tAdding quote to history...")
        self._full_history.append([self._quote, self._image, self._font])
        self._selected_quote = len(self._full_history) - 1

    def update_ui_elements(self):  
    # Make sure that the UI is updated without generating a new image    
        self._generating_quote = True
        # Update other variables and UI elements 
        logger.info("\tUpdating the font colour...")                 
        self.change_colour.setColor('#' + hexify_tuple(self._image[1]))
        logger.info("\tUpdated font colour to RGB" + str(self._image[1]) + ".")
        index_font = self.change_font.findText(self._font[2])
        if index_font >= 0:
            logger.info("\tSelecting new font and font size...")
            self.change_font.setCurrentIndex(index_font)
            self.change_font_size.setCurrentIndex(self.change_font_size.findText(str(self._font[1])))
            logger.info("\tFont name and size updated.")
        self._generating_quote = False

    def create_quote_image(self):
        # Can't create an image without parameters
        if self._image == [] or self._font == [] or self._selected_quote == -1:
            logger.info("Error. Could not generate quote, insufficient parameters.")
            return

        # Prepare the image
        logger.info("\tOpening image...")         
        image_path = os.path.join(current_path, 'images', self._image[0])
        image = Image.open(image_path)

        color = self._image[1]
        location = self._image[2]

        text = self._quote
        font_name = os.path.join(current_path, 'fonts', self._font[0])
        font_custom_size = self._font[1]
        line_height = font_custom_size + 8
        logger.info("\tSetting line height to " + str(line_height) + ".")
        img = ImageText(image, background=(255, 255, 255, 200)) # 200 = alpha
        
        # Determine number of lines
        nr_of_lines = text.count("\n") + 1
        logger.info("\tQuote has " + str(nr_of_lines) + " lines.")
        # Add the separate lines to a list
        lines = text.splitlines()
        x_val = 20 # default indentation
        y_val = 0

        if self._image[3] == 'top':
            x_val += self._image[4]
            y_val = 30 + self._image[5]                
        elif self._image[3] == 'middle':
            x_val += self._image[4]
            y_val = 225 + self._image[5]
            # Make sure the text is centered around the given y value
            y_val -= (nr_of_lines * 35)/2
        elif self._image[3] == 'bottom':
            x_val += self._image[4]
            y_val = 450 + self._image[5]
            # Make sure the text starts high enough
            y_val -= (nr_of_lines * 35)
        else:
            return
        # Assign the resulting offset to x/y
        x = x_val
        y = y_val

        logger.info("\tDrawing quote text...")
        # Now draw each line onto the image
        for line in lines:
            img.write_text_box((x, y), line, box_width=180, font_filename=font_name,
                    font_size=font_custom_size, color=color, place=location)
            y += line_height

        # Save in temporary location
        logger.info("\tSaving temp file...")
        img.save('temp.png')

        # Display the modified image
        logger.info("\tDisplaying image in UI...")
        if os.path.isfile('temp.png'):
            pixmap = QPixmap('temp.png')
        else:
            logger.info("Temporary image quote file not found.")
        self.quote_area.resize(pixmap.width(), pixmap.height())
        self.quote_area.setPixmap(pixmap)

    def change_selected_font(self):
        # Only update if triggered by a UI event, not when generating a quote
        if not self._generating_quote:
            logger.info("\tChanging selected font...")
        	# A new font has been selected, so pick up the selected item's text
            new_font = self.change_font.currentText()
        	# Find this font in the collection
            for font in self._font_collection:
            	if font[2] == new_font:
                	self._font = font
            logger.info("\tNew font applied: " + new_font + ".")
        	# Re-create the image with the new font setting
        
            self.create_quote_image()

    def change_selected_font_size(self):
        # Only update if triggered by a UI event, not when generating a quote
        if not self._generating_quote:
            logger.info("\tChanging selected font size...")
            if self._font != []:
                new_size = self.change_font_size.currentText()
                self._font[1] = int(new_size)
                logger.info("\tNew font size applied: " + new_size + ".")            
                self.create_quote_image()

    def change_selected_colour(self):
        # Only update if triggered by a UI event, not when generating a quote
        if not self._generating_quote:
            logger.info("\tChanging selected font colour...")
        	# A new colour has been selected, so get the new colour name and save it
            if self._image != None:
            	# Convert to RGB and store 
                self._image[1] = ImageColor.getcolor(self.change_colour.color(), "RGB")
                logger.info("\tNew font colour applied: RGB" + str(self._image[1]) + ".")
            # Re-create the image            
            self.create_quote_image()

    def save_quote(self):
        # Check if there's a generated image present
        logger.info("Saving quote...")
        try:
            if os.path.isfile('temp.png'):
                logger.info("\tCreating save dialog...")
                # Create a dialog in which to select a name and location
                self.save_dialog = QFileDialog()
                save_file_name = self.save_dialog.getSaveFileName(self, 'Save quote', '', filter='Image files (.png)', selectedFilter='*.png')
                save_file = save_file_name[0] + '.png'
                logger.info("\tSaving file as " + save_file + ".")
                # Check if the filename already exists
                if os.path.isfile(save_file):
                    logger.info("\tFilename already exists.")
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
                        logger.info("\tOverwriting existing file...")
                        shutil.copyfile('temp.png', save_file)
                        logger.info("\tFile saved.")
                    else:
                        pass                    
                else:
                    logger.info("\tFile saved.")
                    shutil.copyfile('temp.png', save_file)
        # If no generated image is present, there's nothing to save
            else:
                logger.info("No image file available to save.")
        except FileNotFoundError:
            logger.info("No image file available to save.")

    # Return whether a 'next' quote is available
    def next_available(self):
        return (len(self._full_history) > 1 and self._selected_quote < len(self._full_history) - 1)

    # Return whether a 'previous' quote is available
    def previous_available(self):
        return (len(self._full_history) > 1 and self._selected_quote > 0)

    # Can only save/export if at least one image has been generated
    def history_available(self):
        return (len(self._full_history) > 0)

    # Update the status of the toolbar buttons (enabled based on context)
    def update_toolbar_buttons(self):
        self.button_next_action.setEnabled(self.next_available())
        self.button_previous_action.setEnabled(self.previous_available())
        self.button_export_quotes_action.setEnabled(self.history_available())
        self.button_save_quote_action.setEnabled(self.history_available())

    # What happens when the "Previous" button is clicked
    def previous_quote(self):
        logger.info("Selecting previous quote...")
        # If there's more than one quote and you're not looking at the first quote, you can go back
        if len(self._full_history) > 1 and self._selected_quote >= 1:
            self._selected_quote = self._selected_quote - 1
            self._quote = self._full_history[self._selected_quote][0]
            self._image = self._full_history[self._selected_quote][1]
            self._font = self._full_history[self._selected_quote][2]
            self.change_colour.setColor('#' + hexify_tuple(self._image[1]))
            self.update_ui_elements()
            self.create_quote_image()
            self.update_quote_counter()
            self.update_toolbar_buttons()
            logger.info("Previous quote selected.")
        else:
            logger.info("No previous quote available.")
            return

    # What happens when the "Next" button is clicked
    def next_quote(self):
        logger.info("Selecting next quote...")
        # If you are not looking at the most recent quote, you can go forward
        if self._selected_quote < len(self._full_history) - 1:
            self._selected_quote = self._selected_quote + 1
            self._quote = self._full_history[self._selected_quote][0]
            self._image = self._full_history[self._selected_quote][1]
            self._font = self._full_history[self._selected_quote][2]
            self.change_colour.setColor('#' + hexify_tuple(self._image[1]))              
            self.update_ui_elements()               
            self.create_quote_image()
            self.update_quote_counter()
            self.update_toolbar_buttons()
            logger.info("Next quote selected.")
        else:
            logger.info("No next quote available.")
            return
            
    def update_quote_counter(self):
            self.label_position.setText(str(self._selected_quote + 1) + "/" + str(len(self._full_history)))

    # Export the quote history to a txt file in the current directory - will overwrite without warning.
    def export_quotes(self):
        logger.info("Exporting quote history...")
        with open('dutch_wisdom_quote_collection.txt', 'w') as f:
            for quote in self._full_history:
                f.write(f"{quote[0]}\n\n---\n\n")        
        logger.info("Quote history exported to file.")

    # Determine the available word collection depending on the toggles (NSFW/negative on or off)
    def settings_changed(self):
        logger.info("Updating used word collection...")
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
        if self.button_nsfw_action.isChecked():
            logger.info("\tAdding NSFW words...")
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
            word_collections.people_singular = word_collections.people_singular + word_collections.people_singular_nsfw
            word_collections.people_plural = word_collections.people_plural + word_collections.people_plural_nsfw
        # Add negative stuff
        if self.button_negative_action.isChecked() == True:
            logger.info("\tAdding negative words...")
            word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_negative
            word_collections.concepts = word_collections.concepts + word_collections.concepts_negative
            word_collections.people_singular = word_collections.people_singular + word_collections.people_singular_neg
            word_collections.people_plural = word_collections.people_plural + word_collections.people_plural_neg
        # Remove anything but positive
        if self.button_negative_action.isChecked() == False:
            logger.info("\tRestricting to positive words only...")
            word_collections.adjectives = word_collections.adjectives_positive  
        logger.info("Word collection updated.")  
        logger.info("Exporting current settings to file...")   
        self.export_settings()        
        logger.info("Settings exported.")
    
    # Import the word collection from the files in the folder word_collections
    def import_word_lists(self):
        logger.info("\tImporting word lists...")
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
        word_collections.people_singular_nsfw = word_collections.import_list("people_singular_nsfw.txt")
        word_collections.people_plural_nsfw = word_collections.import_list("people_plural_nsfw.txt")
        word_collections.zodiac = word_collections.import_list("zodiac.txt")
        word_collections.sometimes = word_collections.import_list("sometimes.txt")
        word_collections.cliches_sfw = word_collections.import_list("cliches_sfw.txt")
        word_collections.cliches_nsfw = word_collections.import_list("cliches_nsfw.txt")
        word_collections.food_concepts = word_collections.import_list("food_concepts.txt")
        logger.info("\tWord lists imported.")

    # Export every word list and make sure the words are in alphabetical order.
    # This function is not used by default and is only there as a convenience.
    def export_word_lists(self):
        logger.info("\tExporting word lists...")
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
        word_collections.export_list(word_collections.people_singular_nsfw, "people_singular_nsfw")
        word_collections.export_list(word_collections.people_plural_nsfw, "people_plural_nsfw")
        word_collections.export_list(word_collections.zodiac, "zodiac")
        word_collections.export_list(word_collections.sometimes, "sometimes")
        word_collections.export_list(word_collections.cliches_sfw, "cliches_sfw")
        word_collections.export_list(word_collections.cliches_nsfw, "cliches_nsfw")
        word_collections.export_list(word_collections.food_concepts, "food_concepts.txt")
        logger.info("\tWord lists exported.")

    def export_font_collection(self):
        logger.info("Exporting font collection...")
        font_location = os.path.join(current_path, 'resources', 'font_collection.csv')
        with open(font_location, 'w', newline='') as csvfile:
            fontwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in self._font_collection:
                fontwriter.writerow(line)
        logger.info("Fonts exported.")

    def export_image_collection(self):
        logger.info("Exporting image collection...")
        image_location = os.path.join(current_path, 'resources', 'image_collection.csv')
        with open(image_location, 'w', newline='') as csvfile:
            imagewriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in self._image_collection:
                imagewriter.writerow(line)
        logger.info("Image collection exported.")

    def import_settings(self):
        # Read the settings from file
        settings_location = os.path.join(current_path, 'resources', 'settings.txt')
        if os.path.isfile(settings_location):
            settings = []
            settingsinput = open(settings_location,'r')
            for entry in settingsinput:
                settings.append(entry.rstrip())
            settingsinput.close()
            
            # Check validity (only two entries expected)
            if len(settings) == 2:
                nsfw_setting = settings[0]
                negative_setting = settings[1]
                if nsfw_setting == "True":
                    self.button_nsfw_action.setChecked(True)
                elif nsfw_setting == "False":
                    self.button_nsfw_action.setChecked(False)
                else:
                    logger.info("Could not import NSFW setting.")
                if negative_setting == "True":
                    self.button_negative_action.setChecked(True)
                elif negative_setting == "False":
                    self.button_negative_action.setChecked(False)
                else:
                    logger.info("Could not import Negative setting.")
            else:
                logger.info("Unexpected file content. Could not import settings.")
        else:
            logger.info("Settings file does not exist.")


    def export_settings(self):
        # Write the settings to file
        settings_location = os.path.join(current_path, 'resources', 'settings.txt')
        with open(settings_location, 'w', newline='') as settingsfile:
            settingsfile.write(str(self.button_nsfw_action.isChecked()))
            settingsfile.write("\n")
            settingsfile.write(str(self.button_negative_action.isChecked()))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    stylesheet_path = os.path.join(current_path, 'resources', 'style.qss')
    qss = Path(stylesheet_path).read_text()

    qdarktheme.setup_theme("dark", custom_colors={"primary": "#2b8d94"}, additional_qss=qss)
    app.setStyle('fusion')

    logging.basicConfig(filename='quotatas.log', level=logging.INFO)

    logging.info("\n\n-------------------\nStarting application!-------------------\n\n")

    window = MainWindow()
    window.show()

    app.exec()
