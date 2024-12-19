#building off the previous script by adding several color widgets

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget)

from layout_colorwidget import Color #importing our custom class!

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # creates a layout as an instance of the QVBoxLayout class, then adds our custom widget
        layout = QVBoxLayout()
        #this time, adding several color widgets
        layout.addWidget(Color("red"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("green"))

        #creates a dummy widget, assigns our layout to it, then sets it as the central widget for display
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()