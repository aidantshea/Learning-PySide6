from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #creates a button that when pushed, sends a signal to a slot method
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)
    
    #method that literally just prints "Clicked!" to terminal 
    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()