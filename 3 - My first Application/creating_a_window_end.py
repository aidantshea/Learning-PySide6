#adding size restriction to window

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300)) #setting window to a fixed size
        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()