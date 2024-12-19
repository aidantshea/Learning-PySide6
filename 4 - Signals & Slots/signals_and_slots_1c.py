# storing the checkstate of the button as a local variable

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.checkstate = True #setting default value for variable to True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.checkstate) # sets initial state of widget, which should just be our default value

        self.setCentralWidget(button)
    
    # this method updates the local variable's value to the widgets checkstate and prints to terminal
    def the_button_was_toggled(self, checked):
        self.checkstate = checked
        print(self.checkstate)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()