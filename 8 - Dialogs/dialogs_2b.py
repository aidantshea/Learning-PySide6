# combining scripts 1b and 2a to run our custom dialog

from dialogs_2a import CustomDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)
    
    # this method 1.) outputs information to terminal 2.) generates an instance of the custom dialog and runs it
    def button_clicked(self, s):
        print("Click!", s)

        dlg = CustomDialog(self) #passing the MainWindow object as the 'parent' paramter for window centering
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel")
                      

app = QApplication([])

window = MainWindow()
window.show()

app.exec()