#creating a simple button, modifying in the next script to include a dialog

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)
    
    def button_clicked(self, s):
        print("Click!", s)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()