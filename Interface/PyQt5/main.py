import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout,
                             QLabel, QPushButton, QTextEdit)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()



root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
