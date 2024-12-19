# finshing dialogs_file_3 by completing the 4 slot methods corresponding to the buttons

import os
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

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
    
    # this method opens a dialog, reads the filename selected and the active filter, then prints to terminal along w/ the file's contents
    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        # adding additional keyword arguments for caption and dir; an empty string sets these to the default
        filename, active_filter = QFileDialog.getOpenFileName(self, filter=filters, selectedFilter=initial_filter, caption="", dir="")
        print("filename:", filename)
        print("active filter:", active_filter)

        # prints the contents of the selected file to terminal
        if filename:
            with open(filename, "r") as f:
                file_contents = f.read()
                print(file_contents)

    # analogous method to get_filenames above; this method handles multiple file selections
    def get_filenames(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        # adding additional keyword arguments for caption and dir; an empty string sets these to the default
        filenames, active_filter = QFileDialog.getOpenFileNames(self, filter=filters, selectedFilter=initial_filter, caption="", dir="")
        print("filenames:", filenames)
        print("active filter:", active_filter)

        # prints the contents of the selected file to terminal
        for file in filenames:
            with open(file, "r") as f:
                file_contents = f.read()
                print(file_contents)
    
    # this method opens a file dialog and saves a file to the directory specified by the user
    def get_save_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        # adding additional keyword arguments for caption and dir; an empty string sets these to the default
        filename, active_filter = QFileDialog.getSaveFileName(self, filter=filters, selectedFilter=initial_filter, caption="", dir="")
        print("filenames:", filename)
        print("active filter:", active_filter)

        # saving the file 
        if filename:
            with open(filename, "w") as f:
                file_content = "example text PySide6"
                f.write(file_content)

    # this method pulls the name of a selected folder and prints to terminal
    def get_folder(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        # gets name of selected folder and prints to terminal
        filename = QFileDialog.getExistingDirectory(self, caption="", dir="")
        print("filename:", filename)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()