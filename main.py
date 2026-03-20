# This Python file uses the following encoding: utf-8
import sys
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

            layout = QVBoxLayout()
            layout.addWidget(self.button)
            layout.addWidget(self.quote_field)
            layout.addWidget(self.positive_toggle)
            layout.addWidget(self.negative_toggle)
            layout.addWidget(self.nsfw_toggle)
            layout.addWidget(self.darkmode_toggle)

            container = QWidget()
            container.setStyleSheet('background-color: orange; color:black; border: 2px solid black; font-size: 24px; padding: 4px;')
            container.setLayout(layout)

            self.setCentralWidget(container)      

        # Define what happens when the button is pressed
        def the_button_was_clicked(self):
            # Select a random quote function from the list and let it return a quote
            self.quote = random.choice(function_collection.function_list)()
            # Show the new quote on the screen
            self.quote_field.setText(self.quote)

        def settings_changed(self):
            word_collections.nouns_singular = word_collections.neutral_nouns_singular + word_collections.people_singular + word_collections.animals_singular + word_collections.verbs_active
            word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.neutral_nouns_plural
            word_collections.adjectives = word_collections.positive_adjectives + word_collections.neutral_adjectives
            word_collections.verbs = word_collections.neutral_verbs
            word_collections.verbs_3p = word_collections.verbs_third_person
            word_collections.verbs_ing = word_collections.verbs_ing_neutral
            if self.nsfw_toggle.isChecked():
                word_collections.nouns_singular = word_collections.nouns_singular + word_collections.nsfw_nouns_singular + word_collections.animals_singular + word_collections.verbs_active + word_collections.nsfw_verbs_active
                word_collections.nouns_plural = word_collections.animals_plural + word_collections.people_plural + word_collections.neutral_nouns_plural + word_collections.nsfw_nouns_plural
                word_collections.adjectives = word_collections.positive_adjectives + word_collections.neutral_adjectives + word_collections.nsfw_adjectives
                word_collections.verbs = word_collections.verbs + word_collections.nsfw_verbs
                word_collections.verbs_3p = word_collections.verbs_third_person + word_collections.nsfw_verbs_third_person
                word_collections.verbs_ing = word_collections.verbs_ing_neutral + word_collections.nsfw_verbs_ing
            if self.negative_toggle.isChecked():
                word_collections.adjectives = word_collections.adjectives + word_collections.negative_adjectives
                self.positive_toggle.setChecked(False)
            if self.positive_toggle.isChecked():
                word_collections.adjectives = word_collections.positive_adjectives
                self.negative_toggle.setChecked(False)

        def updatestylesheet(self):
    	    if self.darkmode_toggle.isChecked():
    		    self.quote_field.setStyleSheet('background-color: #2e2e2e; color: #9e9e9e ;')
    	    else:
    		    self.quote_field.setStyleSheet('background-color: white; color: black;')

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
