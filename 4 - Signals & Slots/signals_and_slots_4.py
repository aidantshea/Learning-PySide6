# in this script, we create two widgets that interact with one another

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()

        # this code causes a signal to be sent when the text is changed on the specified input object
        # this signal is then received by a slot method, which is just the label objects predefined setText method
        self.input.textChanged.connect(self.label.setText)

        # because we're using more than one widget, we'll need a layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()