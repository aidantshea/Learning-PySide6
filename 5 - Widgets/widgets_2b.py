# this script improves on the file path logic for the cat image

import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

basedir = os.path.dirname(__file__) #this code pulls the parent folder of the running script
print("Current Working Directory:", os.getcwd())
print("This script is located in:", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(basedir, "cat.jpg"))) #combines parent folder of script w/ name of file to form file path
        widget.setScaledContents(True) # allows image rescaling

        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()