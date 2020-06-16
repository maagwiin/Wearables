import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QTextEdit, QComboBox, QGraphicsView)
from PyQt5.QtGui import QIcon

from src.lid import Lid
from src.com import Com
from src.log import Log
from src.plot import Plot


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.settings()
        self.create_widgets()
        self.set_layout()

    def settings(self):
        self.setWindowTitle("Interface De Monitoramento - Wearables Gases - NERA")
        self.setWindowIcon(QIcon("./static/icon.svg"))
        self.setFixedSize(1200, 700)
    
    def create_widgets(self):
        self.lid = Lid(self)
        self.com = Com(self)
        self.log = Log(self)


    def set_layout(self):
        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.lid, 0, 0, 1, 2)
        self.main_layout.addWidget(self.com, 1, 0, 1, 2)
        self.main_layout.addWidget(self.log, 2, 0, 2, 1)
        #self.main_layout.addWidget(self.lpg_chart_view, 2, 1, 1, 1)
        #self.main_layout.addWidget(self.co_chart_view, 3, 1, 1, 1)
        self.setLayout(self.main_layout)


root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
