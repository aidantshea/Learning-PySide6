# doing the same thing as in layout_2.py, but with a horizontal layout

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow, QWidget)
from layout_colorwidget import Color    #importing the custom color widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        layout = QHBoxLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()