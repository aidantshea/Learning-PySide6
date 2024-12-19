# this script demonstrates the QLabel widget

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello!")
        
        # setting the font by generating the default, modifying it, then passing it back
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        
        #specifying alignment using a flag from the Qt namespace
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget) 

app = QApplication([])

window = MainWindow()
window.show()

app.exec()