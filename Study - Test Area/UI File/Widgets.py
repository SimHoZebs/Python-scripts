from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")
        self.width = 640
        self.height = 480

        qlabel_text = QLabel("Hello")
        font = qlabel_text.font()
        font.setPointSize(30)
        qlabel_text.setFont(font)
        qlabel_text.setAlignment(Qt.AlignHCenter)

        qlabel_pic = QLabel()
        pixmap = QPixmap("C:/Users/simho/OneDrive - konkuk.ac.kr/Python scripts/Study - Test Area/UI File/cat.jpg")
        qlabel_pic.setPixmap(pixmap)
        #image stretches bigger but not smaller to match window size
        qlabel_pic.setScaledContents(True)

        qcheckbox = QCheckBox()
        qcheckbox.setTristate(True)
        #Qt.PartiallyChecked overrides .setTriState's value
        qcheckbox.setCheckState(Qt.PartiallyChecked)
        #Signals int on state change
        qcheckbox.stateChanged.connect(self.onChange)
        
        qcombobox = QComboBox()
        qcombobox.addItems(['One', '2', 3, '4'])
        #Signals item change (without [str], prints index instead)
        qcombobox.currentIndexChanged[str].connect(self.onChange)
        #Allows users to enter new items in the box
        qcombobox.setEditable(True)
        #If .seteditable, item order is as below.
        #Does not affect default items.
        qcombobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        widgets = [
                    qlabel_text,
                    qlabel_pic,
                    qcheckbox,
                    qcombobox,
                    QDateEdit(),
                    QDateTimeEdit(),
                    QDial(),
                    QDoubleSpinBox(),
                    QFontComboBox(),
                    QLCDNumber(),
                    QLineEdit(),
                    QProgressBar(),
                    QPushButton(),
                    QRadioButton(),
                    QSlider(),
                    QSpinBox(),
                    QTimeEdit()]
        
        layout = QVBoxLayout()

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def onChange(self, s):
        print(s)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# import ipdb; ipdb.set_trace()
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event
# loop has stopped.
