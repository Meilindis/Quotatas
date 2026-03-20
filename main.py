# This Python file uses the following encoding: utf-8
import sys
import os
import random

# A file containing lists of words to be used in quotes, sorted by type
import word_collections

# A file containing the functions that can define different quote structures
import function_collection

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QCheckBox, QHBoxLayout


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
            self.button.setStyleSheet('height: 50px; background-color: #b0cceb; color: black; text-align: center;')

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
            layoutV.addWidget(self.button)
            layoutV.addWidget(self.quote_field)
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

        # Define what happens when the button is pressed
        def the_button_was_clicked(self):
            # Set the selected quote to the last one (in case the user was looking at an earlier quote)
            if len(self.quote_history) > 1:
                self.selected_quote = len(self.quote_history) - 1
            # Adding new quote, so exporting makes sense again
            self.button_export_quotes.setText("Export session quotes")

            # Select a random quote function from the list and let it return a quote
            self.quote = random.choice(function_collection.function_list)()
            # Add it to the quote history
            self.quote_history.append(self.quote)
            # Set the selected quote index to this new quote's index
            self.selected_quote = len(self.quote_history) - 1
            # Show the new quote on the screen
            self.quote_field.setText(self.quote)

        def settings_changed(self):
            # Set all word collections to neutral
            word_collections.nouns_singular = word_collections.neutral_nouns_singular + word_collections.people_singular + word_collections.animals_singular + word_collections.verbs_active
            word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.neutral_nouns_plural
            word_collections.adjectives = word_collections.positive_adjectives + word_collections.neutral_adjectives
            word_collections.verbs = word_collections.neutral_verbs
            word_collections.verbs_3p = word_collections.verbs_third_person
            word_collections.verbs_ing = word_collections.verbs_ing_neutral
            # Add NSFW
            if self.nsfw_toggle.isChecked():
                word_collections.nouns_singular = word_collections.nouns_singular + word_collections.nsfw_nouns_singular + word_collections.animals_singular + word_collections.verbs_active + word_collections.nsfw_verbs_active
                word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.neutral_nouns_plural + word_collections.nsfw_nouns_plural
                word_collections.adjectives = word_collections.positive_adjectives + word_collections.neutral_adjectives + word_collections.nsfw_adjectives
                word_collections.verbs = word_collections.verbs + word_collections.nsfw_verbs
                word_collections.verbs_3p = word_collections.verbs_third_person + word_collections.nsfw_verbs_third_person
                word_collections.verbs_ing = word_collections.verbs_ing_neutral + word_collections.nsfw_verbs_ing
            # Add negative stuff
            if self.negative_toggle.isChecked():
                word_collections.adjectives = word_collections.adjectives + word_collections.negative_adjectives
                # You cannot select both negative and positive
                self.positive_toggle.setChecked(False)
            # Remove anything but positive
            if self.positive_toggle.isChecked():
                word_collections.adjectives = word_collections.positive_adjectives
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

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
