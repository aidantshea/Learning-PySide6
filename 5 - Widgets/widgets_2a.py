# the QLabel widget may also be used to show images!

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(r"C:\Python Shelly\TutorialPySide6\5 - Widgets\cat.jpg"))

        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()