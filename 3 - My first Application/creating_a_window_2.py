# note that any QtWidget can be a window, for example this pushable button
# cool, but not useful

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])

window = QPushButton("Push Me!")
window.show()

app.exec()