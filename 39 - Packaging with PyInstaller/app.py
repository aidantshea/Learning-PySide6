from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
from PySide6.QtGui import QIcon; from PySide6.QtCore import QSize
import os, sys

basedir = os.path.dirname(__file__)

# providing windows with an application identifier, which prevents windows from just giving it a python icon
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Hello World")
        layout = QVBoxLayout()

        label = QLabel("My Simple App")
        label.setMargin(10)
        layout.addWidget(label)

        button_close = QPushButton("Close")
        button_close.setIcon(QIcon(os.path.join(basedir, "icons", "icon.png"))) #creates icon for the button itself
        button_close.pressed.connect(self.close)
        layout.addWidget(button_close)
        
        button_maximize = QPushButton("Maximize")
        button_maximize.setIcon(QIcon(os.path.join(basedir, "icons", "icon2.png")))
        layout.addWidget(button_maximize)

        container = QWidget()
        container.setLayout(layout)
        container.setFixedSize(QSize(300, 150))
        
        self.setCentralWidget(container)
        self.show()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icon_exec.ico"))) #creates icon for application window
w = MainWindow()
app.exec()

# PyInstaller --windowed app.py --add-data "icons:icons" --icon icon_exec.ico -y