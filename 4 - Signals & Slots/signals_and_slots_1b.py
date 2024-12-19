#modified method from before to also print checkstate of button 

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        
        # causes clicking the button to send a signal to the two referenced slot methods
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)
    
    # this method prints "Clicked!" to terminal
    def the_button_was_clicked(self):
        print("Clicked!")
    
    # this method prints the checkstate to terminal
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()