# This Python file uses the following encoding: utf-8
import sys
import os
import random
from pathlib import Path

# A file containing lists of words to be used in quotes, sorted by type
import word_collections

# A file containing the functions that can define different quote structures
import function_collection

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout

def import_word_lists():
    word_collections.adjectives_positive = word_collections.import_list('adjectives_positive.txt')
    word_collections.adjectives_negative = word_collections.import_list("adjectives_negative.txt")
    word_collections.adjectives_neutral = word_collections.import_list("adjectives_neutral.txt")
    word_collections.colours = word_collections.import_list("colours.txt")
    word_collections.nouns_singular_sfw = word_collections.import_list("nouns_singular_sfw.txt")
    word_collections.nouns_plural_sfw = word_collections.import_list("nouns_plural_sfw.txt")
    word_collections.people_singular = word_collections.import_list("people_singular.txt")
    word_collections.people_plural = word_collections.import_list("people_plural.txt")
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


if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Store the quote here:
            self.quote = ""

            self.setWindowTitle("Dutch Wisdom Bot")

            # Button to generate quotes
            self.button = QPushButton("Give me some wisdom!")
            self.button.setCheckable(True)
            self.button.clicked.connect(self.the_button_was_clicked)
            self.button.setStyleSheet('height: 80px; background-color: #b0cceb; color: black; text-align: center;')

            # Field that displays the generated quote
            self.quote_field = QTextEdit()
            self.quote_field.setReadOnly(True)
            self.quote_field.setStyleSheet('background-color: white; color: black;')

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

            self.positive_toggle = QCheckBox(text="Positive only, build me up!")
            self.positive_toggle.stateChanged.connect(self.settings_changed)
            self.positive_toggle.setStyleSheet('background-color: #b0ebc3;')
            
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
            layoutV.addWidget(self.quote_field)
            layoutV.addWidget(self.button)
            layoutV.addWidget(nav_container)
            layoutV.addWidget(self.positive_toggle)
            layoutV.addWidget(self.negative_toggle)
            layoutV.addWidget(self.nsfw_toggle)
            layoutV.addWidget(self.darkmode_toggle)
            layoutV.addWidget(self.button_export_quotes)

            container = QWidget()
            container.setStyleSheet('background-color: #808080; color:black; border: 2px solid black; font-size: 24px; padding: 4px;')
            container.setLayout(layoutV)

            self.setCentralWidget(container)    

            self.quote_history = []
            self.selected_quote = 0

            import_word_lists()
            self.settings_changed()
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
            # Show the new quote on the screen
            self.quote_field.setText(self.quote)

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
            # Add negative stuff
            if self.negative_toggle.isChecked():
                word_collections.adjectives = word_collections.adjectives + word_collections.adjectives_negative
                word_collections.concepts = word_collections.concepts + word_collections.concepts_negative
                # You cannot select both negative and positive
                self.positive_toggle.setChecked(False)
            # Remove anything but positive
            if self.positive_toggle.isChecked():
                word_collections.adjectives = word_collections.adjectives_positive
                # You cannot select both negative and positive
                self.negative_toggle.setChecked(False)

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
            else:
                return
        def next_quote(self):
            # If you are not looking at the most recent quote, you can go forward
            if self.selected_quote < len(self.quote_history) - 1:
                self.selected_quote = self.selected_quote + 1
                self.quote = self.quote_history[self.selected_quote]
                self.quote_field.setText(self.quote)
            else:
                return

        def export_quotes(self):
            # Export the quote history to a txt file in the current directory - will overwrite without warning!
            with open('dutch_wisdom_quote_collection.txt', 'w') as f:
                for quote in self.quote_history:
                    f.write(f"{quote}\n\n---\n\n")

            self.button_export_quotes.setText("Exported!")

        def export_word_lists(self):
            # Export every word list and make sure the words are in alphabetical order
            word_collections.export_list(word_collections.adjectives_positive, "adjectives_positive")
            word_collections.export_list(word_collections.adjectives_negative, "adjectives_negative")
            word_collections.export_list(word_collections.adjectives_neutral, "adjectives_neutral")
            word_collections.export_list(word_collections.colours, "colours")
            word_collections.export_list(word_collections.nouns_singular_sfw, "nouns_singular_sfw")
            word_collections.export_list(word_collections.nouns_plural_sfw, "nouns_plural_sfw")
            word_collections.export_list(word_collections.people_singular, "people_singular")
            word_collections.export_list(word_collections.people_plural, "people_plural")
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

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
