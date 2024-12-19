# to create a custom window, the best approach is to subclass QMainWindow and include setup in the __init__ block.
# this way, the window behavior is self-contained

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# subclassing QMainWindow to make a custom window. calling it 'MainWindow' for simplicity
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #creates a button and sets it as the central widget of the main window
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

app = QApplication()

window = MainWindow()
window.show()

app.exec()