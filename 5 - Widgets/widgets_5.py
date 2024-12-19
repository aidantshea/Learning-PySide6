# exploring the QList widget

from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        widget = QListWidget()
        widget.addItems(["Aaron", "Barry", "Charles"])
        
        widget.currentItemChanged.connect(self.item_changed) #sends the QList item
        widget.currentTextChanged.connect(self.text_changed) #sends the text of the current item
        
        self.setCentralWidget(widget)
    
    def item_changed(self, i): # i is NOT an index here, it is a QListItem
        print(i.text())
    
    def text_changed(self, s): # s passed as a string
        print(s)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
