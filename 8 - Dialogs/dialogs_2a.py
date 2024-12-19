from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

# A custom dialog class, inherits from QDialog superclass
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) #implementing a parent parameter for dialog window centering

        self.setWindowTitle("Hello!")

        # implementing premade buttons and adding to a buttonBox object
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(buttons)
        
        # user input to accept/reject prompt causes a signal to the accept/reject methods
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # setting widget layout, adding error message as QLabel, adding buttons for user input
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)