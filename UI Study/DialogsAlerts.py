from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# Only needed for access to command line arguments
import sys


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        qcheckbox = QCheckBox()
        qcheckbox.stateChanged.connect(self.onMyToolBarButtonClick)

        layout = QVBoxLayout()
        layout.addWidget(qcheckbox)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()