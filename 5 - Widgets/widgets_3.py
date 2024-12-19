# exploring the QCheckbox widget

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox!")
        widget.setCheckState(Qt.Checked) #setting the initial state of the checkbox as checked
        #widget.setTristate(True)
        widget.stateChanged.connect(self.show_state) #causing changes in checkstate to activate the show_state method

        self.setCentralWidget(widget)
    
    #this method prints the checkstate of the widget to terminal
    def show_state(self, s):
        print(s == 2) #the box stored checkstate in an int from 0-2, this comparison is true when the box is fully checked
        print(s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()