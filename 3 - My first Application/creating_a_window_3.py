#PySide6 comes with a main window widget

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow()
window.show()

app.exec()