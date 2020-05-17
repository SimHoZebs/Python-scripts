import sys

from PySide2.QtWidgets import QApplication, QLabel, QMainWindow
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.windowTitleChanged.connect(self.onWindowTitleChange)
        # self.windowTitleChanged.connect(self.my_custom_fn)
        # self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        # self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a="HELLO!", b=5):
        print(a, b)
    
    def contextMenuEvent(self, event):
        super(MainWindow, self).contextMenuEvent(event)
        print("Context menu event!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
