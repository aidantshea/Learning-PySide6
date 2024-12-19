# extending dialogs_file_2 to add buttons to the application for several file handling tasks

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget

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
        layout = QVBoxLayout()

        # adding 4 buttons, which each activate a corresponding slot method
        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)
        
        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)
        
        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        # passing the layout w/ the 4 buttons to a container widget, then setting the container as the central widget of the application
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    # this method opens a dialog, then identifies the filename of the file selected and the active filter, then prints them to terminal
    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS) #formatting the list of filters to Qt convention

        # adding additional keyword arguments for list of filters and initial filter
        filename, active_filter = QFileDialog.getOpenFileName(self, filter=filters, selectedFilter=initial_filter)
        print("filename:", filename)
        print("active filter:", active_filter)

    def get_filenames(self):
        pass
    
    def get_save_filename(self):
        pass

    def get_folder(self):
        pass

app = QApplication([])

window = MainWindow()
window.show()

app.exec()