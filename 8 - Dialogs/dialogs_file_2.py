# building on dialogs_file_1 to implement file filters

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "All files (*)"
]

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
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS) #formatting the list of filters to Qt convention

        # adding additional keyword arguments for list of filters and initial filter
        filename, active_filter = QFileDialog.getOpenFileName(self, filter=filters, selectedFilter=initial_filter)
        print("filename:", filename)
        print("active filter:", active_filter)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()