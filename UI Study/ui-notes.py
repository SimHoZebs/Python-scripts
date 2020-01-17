"sys is imported optionally, in case the program will use system commands."
import sys

"""
Below are neccessary imports for creating a window.
"""
from PySide2 import
"QtGui: contains QIcon; a function to display app icon image."
from PySide2.QtWidgets import
"QMainWindow: Core class to inherit for the class on display"
"QApplication: To Initialize and exit window"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        ""

