# this method also stores the checkstate of the button to a local variable
# this time though, we don't need to pass the checkstate to the method

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.checkstate = True # initial checkstate local variable value

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.checkstate) # setting initial checkstate to value of local variable above

        self.setCentralWidget(self.button)

    # this method updates the checkstate local variable to the checkstate of the button
    def the_button_was_released(self):
        self.checkstate = self.button.isChecked()
        print(self.button.isChecked())

app = QApplication([])

window = MainWindow()
window.show()

app.exec()