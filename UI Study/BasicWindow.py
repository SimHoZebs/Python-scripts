import sys
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("My Awesome App")

		label = QLabel("This is a PySide2 window!")
		label.setAlignment(Qt.AlignCenter)

		label2 = QLabel("This is another window!")
		label2.setAlignment(Qt.AlignBottom)

		self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()