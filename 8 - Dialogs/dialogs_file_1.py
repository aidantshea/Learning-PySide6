# this application explores QFileDialog's built-in getOpenFileName function, which returns the selected file's name and the currently active file filter

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #creating a button that activates the get_filename method when pressed
        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)
    
    # this method opens a dialog, then identifies the filename of the file selected and the active filter, then prints them to terminal
    def get_filename(self):
        filename, active_filter = QFileDialog.getOpenFileName(self)
        print("filename:", filename)
        print("active filter:", active_filter)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()