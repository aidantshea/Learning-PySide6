#exploring the QComboBox widget

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["Apple", "Banana", "Cupcape"])
        
        #allows editing of the QComboBox
        #widget.setEditable(True)
        #widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        #widget.setMaxCount(10)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    # this method prints the index of the list item the user selects in the QComboBox
    def index_changed(self, i):
        print(i)
    
    # this method prints the string contained in the list item the user selects in the QComboBox
    def text_changed(self, s):
        print(s)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()