import sys
import os
import random
from pathlib import Path
import shutil

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# A file containing lists of words to be used in quotes, sorted by type
import word_collections

# A file containing the templates that define different quote structures
import template_collection

# Script that helps with putting text on images
from image_utils import ImageText

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout, QFileDialog, QMessageBox

# ---------------------------------------------------------------------------------------------------------------------------------------------
# RESOURCES

# Font list: font name, font size that usually fits
font_collection = [
                   ['SuperJoyful-lxwPq.ttf', 26], # Free for commercial use
                   ['SuperChiby-BL62V.ttf', 30],
                   ['MouldyCheeseRegular-WyMWG.ttf', 26],
                   ['SparkyStonesRegular-BW6ld.ttf', 30],
                   ['SuperLarky-nALLR.ttf', 20],
                   ['Martius-LV9L4.ttf', 32],
                   ['BorderWall-OG55o.otf', 26],
                   ['SuperSalad-qZgvV.ttf', 30],
                   ['MangabeyRegular-rgqVO.otf', 30],
                   ['SuperChips-5yBYL.ttf', 26],
                   ['AmberyGardenRegular-PKjGd.ttf', 26],
                   ['Wiltype-9MA1y.ttf', 32],
                   ['Excludeditalic-jEr99.ttf', 20],
                   ['Playball-q6o1.ttf', 30],
                   ['SandanaRegular-JR5q7.ttf', 24]
                   ]

# Image list: image name, text colour, placement, position, extra indentation for x, y (can be negative)
# Default positions:
# Top: 20, 30
# Middle: 20, 225
# Bottom: 20, 450
image_collection = [['a_fetters_recto_b_several_figures_verso.png', (145, 0, 140), 'justify', 'bottom', 0, 0],
                    ['a_luncheon_party_.png', (255, 245, 185), 'justify', 'bottom', 0, 0],
                    ['angel.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['annoyed.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['angry_lady.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['angry.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['ascent.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['babushka.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['balloons.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['bananas.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['bat.png', (255, 245, 185), 'justify', 'bottom', 0, -20],
                    ['bicycle.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['bigsplash.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['blossoms.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['candle.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['cat_snow.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['clown.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['chess.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['chocolate.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['coffee.png', (255, 245, 185), 'justify', 'bottom', 0, 0],
                    ['couple_mountains.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['building_the_freidrich-strasse_station.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['dancer.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['desert.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['die_komponistin_sonia_friedman.png', (167, 255, 174), 'justify', 'bottom', 10, -40],
                    ['dog.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['dogbubbles.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['dogtrick.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['duck.png', (29, 37, 82), 'justify', 'bottom', 0, 0],
                    ['ducklings.png', (255, 255, 255), 'justify', 'bottom', 0, -45],
                    ['earth.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['flysex.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['frogs.png', (255, 255, 255), 'justify', 'bottom', 0, -45],
                    ['galaxy.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['giraffe.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['ghosts.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['glitter.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['goats.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['hare.png', (255, 255, 255), 'justify', 'bottom', 0, 0],
                    ['heart_cloud.png', (29, 37, 82), 'justify', 'top', 0, -50],
                    ['hearts.png', (29, 37, 82), 'justify', 'top', 0, -50],
                    ['horse.png', (29, 37, 82), 'justify', 'middle', 40, 0],
                    ['jellyfish.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['joy.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['juggler.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['kale.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['ladybug.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['les_amateurs_d_estampes.png', (207, 220, 255), 'justify', 'top', 20, 0],
                    ['lonelybot.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['manager.png', (255, 255, 255), 'justify', 'bottom', 0, 0],
                    ['mannekenpis.png', (167, 255, 174), 'justify', 'bottom', 0, 0],
                    ['marx.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['megaphone.png', (29, 37, 82), 'justify', 'top', 40, 0],
                    ['milky_way.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['monkey.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['monster.png', (255, 255, 255), 'justify', 10, 70],
                    ['pancakes.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['pear.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['pepper.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['problem.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['puffin.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['rabbit.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['rain_people.png', (29, 37, 82), 'justify', 'bottom', 0, 20],
                    ['rainbow.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['reading.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['reflection.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['rider.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['robot.png', (199, 17, 234), 'justify', 'top', 0, 0],
                    ['rubberducks.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['silhouettes.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['socks.png', (255, 255, 255), 'justify', 'middle', 0, 0],
                    ['spices.png', (255, 255, 255), 'justify', 'bottom', 0, -45],
                    ['squirrel.png', (255, 255, 255), 'justify', 'bottom', 0, 0],
                    ['staircase.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['stop.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['sunset.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['tea.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['the_tournament.png', (255, 245, 215), 'justify', 'top', 0, 0],
                    ['the_visit_.png', (142, 255, 221), 'justify', 'bottom', 0, 0],
                    ['three_girls_in_profile.png', (24, 0, 59), 'justify', 'bottom', 0, 0],
                    ['top.png', (65, 75, 139), 'justify', 'top', 0, 0],
                    ['treefrog.png', (199, 17, 234), 'justify', 'bottom', 0, 0],
                    ['tulips.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['twelve_men_.png', (199, 17, 234), 'justify', 'top', 10, 0],
                    ['vampire.png', (255, 255, 255), 'justify', 'top', 0, 0],
                    ['woman.png', (255, 245, 185), 'justify', 'top', 0, 0],
                    ['woman_flowers.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ['yarn.png', (29, 37, 82), 'justify', 'top', 0, 0],
                    ]

# ----------------------------------------------------------------------------------------------------------------------
# MAIN PROGRAM

if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # SET UP THE USER INTERFACE

            self.setWindowTitle("Quotatas")

            # CREATE UI COMPONENTS
            # Button to generate quotes
            self.button = QPushButton("Give me some wisdom!")
            self.button.setCheckable(True)
            self.button.clicked.connect(self.the_button_was_clicked)
            self.button.setStyleSheet('height: 80px; background-color: #b0cceb; color: black; text-align: center;')

            # Label that displays the generated quote image
            self.quote_area = QLabel()
            self.quote_area.setStyleSheet('background-color: black; color: white;')
            self.quote_area.resize(500, 500)
            current_dir = Path(__file__).parent.absolute()
            pixmap = QPixmap(os.path.join(current_dir, os.path.join('images','bot.png')))
            self.quote_area.resize(pixmap.width(), pixmap.height())
            self.quote_area.setPixmap(pixmap)

            # Field that displays the generated quote in text only
            self.text_field = QTextEdit()
            self.text_field.setStyleSheet('background-color: #2e2e2e; color: #9e9e9e;')
            self.text_field.setReadOnly(True)
            self.text_field.resize(pixmap.width(), 350)

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
            
            self.button_export_quotes = QPushButton("Export session quotes")
            self.button_export_quotes.clicked.connect(self.export_quotes)
            self.button_export_quotes.setStyleSheet('background-color: orange; color:black;')

            # CREATE LAYOUTS TO ARRANGE THE UI COMPONENTS
            # Arrange the back/forward buttons horizontally
            layoutH = QHBoxLayout()
            layoutH.addWidget(self.button_back)
            layoutH.addWidget(self.button_save)
            layoutH.addWidget(self.button_forward)
            nav_container = QWidget()
            nav_container.setLayout(layoutH)

            # Arrange all settings elements vertically
            layoutV = QVBoxLayout()       
            layoutV.addWidget(self.negative_toggle)
            layoutV.addWidget(self.nsfw_toggle)
            layoutV.addWidget(self.text_field)    
            layoutV.addWidget(self.button_export_quotes)       

            vert_container = QWidget()
            vert_container.setLayout(layoutV)

            # Add quotes and navigation to their own container
            quoteLayout = QVBoxLayout()
            quoteLayout.addWidget(self.quote_area)
            quoteLayout.addWidget(nav_container)
            quoteLayout.addWidget(self.button)

            quote_container = QWidget()
            quote_container.setLayout(quoteLayout)

            # Combine everything into one layout
            layoutApp = QHBoxLayout()
            layoutApp.addWidget(vert_container)
            layoutApp.addWidget(quote_container)

            # Add the layout to an overall widget
            container = QWidget()
            container.setStyleSheet('background-color: #808080; color:black; border: 2px solid black; font-size: 24px; padding: 4px;')
            container.setLayout(layoutApp)

            self.setCentralWidget(container)    

            # CONTAINERS TO STORE THE SELECTED QUOTES, IMAGES, AND FONTS
            # Store the quote here later:
            self.quote = ""
            self.image = []
            self.font = []
            self.full_history = [] # list of lists, containing [quote, image, font]
            self.selected_quote = 0
            
            # Import the .txt files containing the words that are used
            self.import_word_lists()

            # Update the selected words based on the UI settings
            self.settings_changed()
            # self.export_word_lists() # Only enable when you have added new words to the lists and want to alphabetise them.

        # -----------------------------------------------------------------------------------------------------------------------------
        # MEMBER FUNCTIONS

        # Define what happens when the button is pressed
        def the_button_was_clicked(self):
            self.text_field.setText("")
            # Set the selected quote to the last one (in case the user was looking at an earlier quote)
            if len(self.full_history) > 1:
                self.selected_quote = len(self.full_history) - 1
            # Adding new quote, so exporting makes sense again
            self.button_export_quotes.setText("Export session quotes")
            # Select the random parameters
            self.set_parameters()
            # Create the image
            self.create_quote_image()

            # self.quote_field.setText(self.quote)

        def set_parameters(self):
            # Select the random parameters of the quote
            self.image = random.choice(image_collection)
            self.font = random.choice(font_collection)
            self.quote = random.choice(template_collection.template_list)()

            # Add and set the selected quote index to this new quote's index
            self.full_history.append([self.quote, self.image, self.font])
            self.selected_quote = len(self.full_history) - 1

        def create_quote_image(self):
            # Can't create an image without parameters
            if self.image == [] or self.font == [] or self.selected_quote == -1:
                return

            # Prepare the image
            current_dir = Path(__file__).parent.absolute()            
            image_path = os.path.join(os.path.join(current_dir, 'images'), self.image[0])
            image = Image.open(image_path)

            color = self.image[1]
            location = self.image[2]

            text = self.quote
            font_name = os.path.join(os.path.join(current_dir, 'fonts'), self.font[0])
            font_custom_size = self.font[1]
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
            # Assign the resulting x/y value to x/y
            x = x_val
            y = y_val

            # Now draw each line onto the image
            for line in lines:
                img.write_text_box((x, y), line, box_width=200, font_filename=font_name,
                        font_size=font_custom_size, color=color, place=location)
                y += 35

            # Save in temporary location
            img.save('temp.png')

            # Display the modified image
            pixmap = QPixmap('temp.png')
            self.quote_area.resize(pixmap.width(), pixmap.height())
            self.quote_area.setPixmap(pixmap)

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

        def previous_quote(self):
            # If there's more than one quote and you're not looking at the first quote, you can go back
            if len(self.full_history) > 1 and self.selected_quote >= 1:
                self.selected_quote = self.selected_quote - 1
                self.quote = self.full_history[self.selected_quote][0]
                self.image = self.full_history[self.selected_quote][1]
                self.font = self.full_history[self.selected_quote][2]
                
                self.create_quote_image()
            else:
                return
        def next_quote(self):
            # If you are not looking at the most recent quote, you can go forward
            if self.selected_quote < len(self.full_history) - 1:
                self.selected_quote = self.selected_quote + 1
                self.quote = self.full_history[self.selected_quote][0]
                self.image = self.full_history[self.selected_quote][1]
                self.font = self.full_history[self.selected_quote][2]
                
                self.create_quote_image()
            else:
                return

        def export_quotes(self):
            # Export the quote history to a txt file in the current directory - will overwrite without warning!
            with open('dutch_wisdom_quote_collection.txt', 'w') as f:
                for quote in self.full_history:
                    f.write(f"{quote[0]}\n\n---\n\n")

            self.button_export_quotes.setText("Exported!")
        
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

        def export_word_lists(self):
            # Export every word list and make sure the words are in alphabetical order
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


    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
