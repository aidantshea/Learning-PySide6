from PySide6.QtWidgets import QApplication, QWidget

#creates an instance of QApplication class. only one is needed per app.
app = QApplication([])

#creates a Qt widget, which is our window
window = QWidget()
window.show() #windows are hidden by default

#start event loop
app.exec()