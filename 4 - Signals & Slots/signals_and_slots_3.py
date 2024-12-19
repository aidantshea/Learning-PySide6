# this script changes the button so that it takes on a random title when clicked. If a "4" is rolled, the button deactivates

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

# creating an array of possible window titles
window_titles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.clicks = 0 #tracker for how many times the button has been clicked

        self.setWindowTitle("My App") #initial title will be set to "My App"

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)
    
    # this method changes the window title and prints the change to terminal
    def the_button_was_clicked(self):

        print("The button was clicked!")
        new_window_title = choice(window_titles)
        print("Setting title to:", new_window_title)
        self.setWindowTitle(new_window_title)
    
    # this method prints to terminal any time the window title changes. It kills the button if the new title is "4"
    def the_window_title_changed(self, window_title):
        
        print("The window title has been changed to:", window_title)

        if window_title == "4":
            self.button.setDisabled(True)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()