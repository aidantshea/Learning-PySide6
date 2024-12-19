#this script uses a system of nested layouts to create a complex layout

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        #starting with three layouts. Layouts 2 and 3 will be nested in layout 1
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        #generating layout 2, then nesting inside layout 1
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))
        layout1.addLayout(layout2)

        #adding a standalone widget to layout 1
        layout1.addWidget(Color("green"))

        #generating layout3, then nesting inside layout 1
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))
        layout1.addLayout(layout3)
        
        #passing layout1 to the dummy widget, then setting the dummy widget as the central widget of the app.  
        widget = QWidget()
        widget.setLayout(layout1)
        
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()