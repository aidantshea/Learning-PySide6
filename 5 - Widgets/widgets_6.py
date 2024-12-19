# exploring the QLineEdit Widget, in which users can type input

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(12) #sets maximum length of text
        widget.setPlaceholderText("Enter your text") #sets a placeholder to indicate where the user should type
        
        # widget.setReadOnly(True) # uncomment this to make readonly
        
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        
        self.setCentralWidget(widget)

    #this method sets the widget's text to "Boom!"
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    #this method prints the selected text to terminal upon any change in selection
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    #this method prints the text to terminal upon any change in text
    def text_changed(self, s):
        print("Text changed...")
        print(s)

    #this method prints the text when any edit is made
    def text_edited(self, s):
        print("Text edited...")
        print(s)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()