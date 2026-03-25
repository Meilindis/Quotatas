import sys
import os
import random
from pathlib import Path

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# A file containing lists of words to be used in quotes, sorted by type
import word_collections

# A file containing the templates that define different quote structures
import function_collection

# Script that helps with putting text on images
from image_utils import ImageText

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout

font_collection = ['GalaferaMedium-V4xze.ttf', 
                   'LoveDays-2v7Oe.ttf', 
                   'CronusRound-KA6y.ttf', 
                   'Quaaykop-DYE1R.ttf', 
                   'Wonderbar-pALD.ttf', 
                   'HussarBold-7mRE.otf',
                   'BiotripSerifBold-Jpo3K.ttf',
                   'RomanticAdoreDemoRegular-5yGpj.ttf',
                   'BazigBold-yYRV5.ttf']
# Image list: image name, text colour, placement, indent (x), starting height (y)
image_collection = [['a_fetters_recto_b_several_figures_verso.png', (145, 0, 140), 'justify', 50, 365, 'straight'],
                    ['a_luncheon_party_.png', (255, 245, 185), 'justify', 50, 365, 'straight'],
                    ['angry_lady.jpg', (65, 75, 139), 'justify', 50, 100, 'straight'],
                    ['balloons.jpg', (65, 75, 139), 'justify', 40, 100, 'straight'],
                    ['building_the_freidrich-strasse_station.png', (65, 75, 139), 'justify', 40, 100, 'straight'],
                    ['die_komponistin_sonia_friedman.png', (167, 255, 174), 'justify', 30, 305, 'straight'],
                    ['les_amateurs_d_estampes.png', (207, 220, 255), 'justify', 40, 100, 'straight'],
                    ['rider.png', (0, 0, 0), 'justify', 30, 370, 'straight'],
                    ['the_tournament.png', (255, 245, 215), 'justify', 30, 100, 'straight'],
                    ['the_visit_.png', (142, 255, 221), 'justify', 30, 365, 'straight'],
                    ['three_girls_in_profile.png', (24, 0, 59), 'justify', 30, 365, 'straight'],
                    ['twelve_men_.png', (199, 17, 234), 'justify', 30, 100, 'straight'],
                    ['tegeltje.jpg', (65, 75, 139), 'justify', 60, 225, 'curve']
                    ]

if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Store the quote here:
            self.quote = ""

            self.setWindowTitle("Quotatas")

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
            self.quote_field = QTextEdit()
            self.quote_field.setStyleSheet('background-color: white; color: black;')
            self.quote_field.setReadOnly(True)
            self.quote_field.resize(pixmap.width(), 350)

            # Back and forward buttons
            self.button_back = QPushButton("Previous")
            self.button_back.clicked.connect(self.previous_quote)
            self.button_back.setStyleSheet('background-color: orange; color:black;')

            self.button_forward = QPushButton("Next")
            self.button_forward.clicked.connect(self.next_quote)
            self.button_forward.setStyleSheet('background-color: orange; color:black;')

            # Settings toggles
            self.nsfw_toggle = QCheckBox(text="Include NSFW words")
            self.nsfw_toggle.stateChanged.connect(self.settings_changed)
            self.nsfw_toggle.setStyleSheet('background-color: #ffbcf1;')

            self.negative_toggle = QCheckBox(text="Include negative stuff (risky!)")
            self.negative_toggle.stateChanged.connect(self.settings_changed)
            self.negative_toggle.setStyleSheet('background-color: #ffe8a6;')            
            
            self.darkmode_toggle = QCheckBox("Dark mode")
            self.darkmode_toggle.stateChanged.connect(self.updatestylesheet)
            self.darkmode_toggle.setStyleSheet('background-color: #2e2e2e; color: #9e9e9e;')

            self.button_export_quotes = QPushButton("Export session quotes")
            self.button_export_quotes.clicked.connect(self.export_quotes)
            self.button_export_quotes.setStyleSheet('background-color: orange; color:black;')


            # Arrange the back/forward buttons horizontally
            layoutH = QHBoxLayout()
            layoutH.addWidget(self.button_back)
            layoutH.addWidget(self.button_forward)
            nav_container = QWidget()
            nav_container.setLayout(layoutH)

            # Arrange all elements vertically
            layoutV = QVBoxLayout()       
            layoutV.addWidget(self.negative_toggle)
            layoutV.addWidget(self.nsfw_toggle)
            layoutV.addWidget(self.darkmode_toggle)
            layoutV.addWidget(self.button_export_quotes)
            layoutV.addWidget(self.quote_field)
            layoutV.addWidget(self.button)
            

            vert_container = QWidget()
            vert_container.setLayout(layoutV)

            quoteLayout = QVBoxLayout()
            quoteLayout.addWidget(self.quote_area)
            quoteLayout.addWidget(nav_container)

            quote_container = QWidget()
            quote_container.setLayout(quoteLayout)

            layoutApp = QHBoxLayout()
            layoutApp.addWidget(vert_container)
            layoutApp.addWidget(quote_container)


            container = QWidget()
            container.setStyleSheet('background-color: #808080; color:black; border: 2px solid black; font-size: 24px; padding: 4px;')
            container.setLayout(layoutApp)

            self.setCentralWidget(container)    

            self.quote_history = []
            self.selected_quote = 0

            self.darkmode_toggle.setChecked(True)

            self.import_word_lists()
            self.settings_changed()
            self.updatestylesheet()
            # self.export_word_lists() # Only enable when you have added new words to the lists and want to alphabetise them.

        # Define what happens when the button is pressed
        def the_button_was_clicked(self):
            # Set the selected quote to the last one (in case the user was looking at an earlier quote)
            if len(self.quote_history) > 1:
                self.selected_quote = len(self.quote_history) - 1
            # Adding new quote, so exporting makes sense again
            self.button_export_quotes.setText("Export session quotes")

            # Select a random quote function from the list and let it return a quote
            self.quote = random.choice(function_collection.template_list)()
            # Add it to the quote history
            self.quote_history.append(self.quote)
            # Set the selected quote index to this new quote's index
            self.selected_quote = len(self.quote_history) - 1

            self.create_quote_image()

            self.quote_field.setText(self.quote)

        def create_quote_image(self):
            # Prepare the image
            current_dir = Path(__file__).parent.absolute()
            selected_image = random.choice(image_collection)
            image_path = os.path.join(os.path.join(current_dir, 'images'), selected_image[0])
            image = Image.open(image_path)

            color = selected_image[1]
            location = selected_image[2]
            x_val = selected_image[3] # indent to the right from 0 (base is one line)
            y_val = selected_image[4] # pixels down from zero
            text = self.quote
            font = os.path.join(os.path.join(current_dir, 'fonts'), random.choice(font_collection))
            img = ImageText(image, background=(255, 255, 255, 200)) # 200 = alpha


            if "\n" not in text:
                #write_text_box will split the text in many lines, based on box_width
                #`place` can be 'left' (default), 'right', 'center' or 'justify'
                #write_text_box will return (box_width, box_calculed_height) so you can
                #know the size of the wrote text
                img.write_text_box((x_val, y_val), text, box_width=200, font_filename=font,
                                font_size=24, color=color, place=location) # 60,225
            else:
                nr_of_lines = text.count("\n") + 1
                if nr_of_lines == 2:
                    lines = text.splitlines()
                    if selected_image[5] == 'curve':
                        x = x_val + 5
                    else: x = x_val
                    y = y_val - 25
                    for line in lines:
                        img.write_text_box((x, y), line, box_width=200, font_filename=font,
                                font_size=26, color=color, place=location)
                        y += 35
                elif nr_of_lines == 3:
                    lines = text.splitlines()
                    if selected_image[5] == 'curve':
                        x = x_val + 10
                    else: x = x_val
                    y = y_val - 35
                    for line in lines:
                        img.write_text_box((x, y), line, box_width=200, font_filename=font,
                                font_size=26, color=color, place=location)
                        y += 35
                elif nr_of_lines == 4:
                    lines = text.splitlines()
                    if selected_image[5] == 'curve':
                        x = x_val + 15
                    else: x = x_val
                    y = y_val - 45
                    for line in lines:
                        img.write_text_box((x, y), line, box_width=200, font_filename=font,
                                font_size=26, color=color, place=location)
                        y += 35
                elif nr_of_lines == 5:
                    lines = text.splitlines()
                    if selected_image[5] == 'curve':
                        x = x_val + 20
                    else: x = x_val
                    y = y_val - 55
                    for line in lines:
                        img.write_text_box((x, y), line, box_width=200, font_filename=font,
                                font_size=26, color=color, place=location)
                        y += 35
                elif nr_of_lines == 6:
                    lines = text.splitlines()
                    if selected_image[5] == 'curve':
                        x = x_val + 25
                    
                    else: x = x_valy = y_val - 65
                    for line in lines:
                        img.write_text_box((x, y), line, box_width=200, font_filename=font,
                                font_size=26, color=color, place=location)
                        y += 35


            img.save('temp.png')

            # Display the modified image
            pixmap = QPixmap('temp.png')
            self.quote_area.resize(pixmap.width(), pixmap.height())
            self.quote_area.setPixmap(pixmap)


        def settings_changed(self):
            # Set all word collections to neutral
            word_collections.nouns_singular = word_collections.nouns_singular_sfw + word_collections.people_singular + word_collections.animals_singular + word_collections.verbs_active_sfw + word_collections.food_singular
            word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.nouns_plural_sfw + word_collections.food_plural
            word_collections.adjectives = word_collections.adjectives_positive + word_collections.adjectives_neutral
            word_collections.verbs = word_collections.verbs_sfw
            word_collections.verbs_third_person = word_collections.verbs_third_person_sfw
            word_collections.verbs_ing = word_collections.verbs_ing_sfw
            word_collections.verbs_intransitive = word_collections.verbs_intransitive_sfw
            word_collections.concepts = word_collections.concepts_neutral + word_collections.concepts_positive
            word_collections.comparatives = word_collections.comparatives_sfw
            word_collections.superlatives = word_collections.superlatives_sfw
            word_collections.situations = word_collections.situations_sfw
            word_collections.people_singular = word_collections.people_singular_sfw
            word_collections.people_plural = word_collections.people_plural_sfw
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
                word_collections.adjectives = word_collections.adjectives + word_collections.comparatives_nsfw
                word_collections.comparatives = word_collections.comparatives + word_collections.comparatives_nsfw
                word_collections.superlatives = word_collections.superlatives + word_collections.superlatives_nsfw
                word_collections.situations = word_collections.situations + word_collections.situations_nsfw
            # Add negative stuff
            if self.negative_toggle.isChecked() == True:
                word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_negative
                word_collections.concepts = word_collections.concepts + word_collections.concepts_negative
                word_collections.people_singular = word_collections.people_singular + word_collections.people_singular_neg
                word_collections.people_plural = word_collections.people_plural + word_collections.people_plural_neg
            # Remove anything but positive
            if self.negative_toggle.isChecked() == False:
                word_collections.adjectives = word_collections.adjectives_positive               

        def updatestylesheet(self):
    	    if self.darkmode_toggle.isChecked():
    		    self.quote_field.setStyleSheet('background-color: #2e2e2e; color: #9e9e9e;')
    	    else:
    		    self.quote_field.setStyleSheet('background-color: white; color: black;')

        def previous_quote(self):
            # If there's more than one quote and you're not looking at the first quote, you can go back
            if len(self.quote_history) > 1 and self.selected_quote >= 1:
                self.selected_quote = self.selected_quote - 1
                self.quote = self.quote_history[self.selected_quote]
                self.quote_field.setText(self.quote)
                self.create_quote_image()
            else:
                return
        def next_quote(self):
            # If you are not looking at the most recent quote, you can go forward
            if self.selected_quote < len(self.quote_history) - 1:
                self.selected_quote = self.selected_quote + 1
                self.quote = self.quote_history[self.selected_quote]
                self.quote_field.setText(self.quote)
                self.create_quote_image()
            else:
                return

        def export_quotes(self):
            # Export the quote history to a txt file in the current directory - will overwrite without warning!
            with open('dutch_wisdom_quote_collection.txt', 'w') as f:
                for quote in self.quote_history:
                    f.write(f"{quote}\n\n---\n\n")

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
            word_collections.prepositions = word_collections.import_list("prepositions.txt")
            word_collections.people_singular_neg = word_collections.import_list("people_singular_neg.txt")
            word_collections.people_plural_neg = word_collections.import_list("people_plural_neg.txt")
            word_collections.zodiac = word_collections.import_list("zodiac.txt")
            word_collections.sometimes = word_collections.import_list("sometimes.txt")

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
            word_collections.export_list(word_collections.prepositions, "prepositions")
            word_collections.export_list(word_collections.people_singular_neg, "people_singular_neg")
            word_collections.export_list(word_collections.people_plural_neg, "people_plural_neg")
            word_collections.export_list(word_collections.zodiac, "zodiac")
            word_collections.export_list(word_collections.sometimes, "sometimes")


    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
