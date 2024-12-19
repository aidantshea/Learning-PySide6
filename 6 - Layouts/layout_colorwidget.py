#this script is a custom class for use in the other exersizes of this chapter

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

#subclassing QWidget to create a custom class 'Color', this class accepts one parameter as a string
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True) #tells widget to fill background w/ the window color

        # this widget is a solid-filled widget of whatever color is passed to the class
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)