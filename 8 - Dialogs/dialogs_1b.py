#building off the button to implement a simple dialog

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)
    
    # this method 1.) outputs information to terminal 2.) creates a new dialog and runs it
    def button_clicked(self, s):
        print("Click!", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("???")
        dlg.exec()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()