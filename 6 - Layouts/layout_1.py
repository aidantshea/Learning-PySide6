# implementing the custom Color widget class to an app!

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

# importing the Color class from the first script from this chapter
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = Color("red")
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()