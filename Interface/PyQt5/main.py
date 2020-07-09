import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QTextEdit, QComboBox, QGraphicsView)
from PyQt5.QtGui import QIcon

from src.lid import Lid
from src.com import Com
from src.log import Log
from src.meter import Meter
from src.plot import Plot
from core.exe import Exe


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.settings()
        self.create_widgets()
        self.set_layout()
        self.attvalue()
        

    def settings(self):
        self.setWindowTitle("Interface De Monitoramento - Wearables Gases - NERA")
        self.setWindowIcon(QIcon("./static/icon.svg"))
        self.setFixedSize(1200, 700)
        self.setStyleSheet(
            '* { background: white; }'
        )
    
    def create_widgets(self):
        self.lid = Lid(self)
        self.com = Com(self)
        self.log = Log(self)
        self.lpg_meter = Meter('A', self)
        self.co_meter = Meter('B', self)
        self.lpg_plot = Plot('A', self)
        self.co_plot = Plot('B', self)


    def set_layout(self):
        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.lid, 0, 0, 1, 2)
        self.main_layout.addWidget(self.com, 1, 0, 1, 2)
        self.main_layout.addWidget(self.log, 2, 0, 2, 1)
        self.main_layout.addWidget(self.lpg_meter, 2, 1, 1, 1)
        self.main_layout.addWidget(self.co_meter, 3, 1, 1, 1)
        self.main_layout.addWidget(self.lpg_plot, 4, 0, 5, 1)
        self.main_layout.addWidget(self.co_plot, 4, 1, 5, 1)
        self.main_layout.setRowStretch(0,1)
        self.main_layout.setRowStretch(1,2)
        self.main_layout.setRowStretch(2,3)
        self.main_layout.setRowStretch(3,3)
        self.main_layout.setRowStretch(4,7)
        self.setLayout(self.main_layout)

    def attvalue(self):
        self.core = Exe(self)

root = QApplication(sys.argv)
app = MainWindow()
root.setWindowIcon(QIcon("./static/icon.svg"))
app.show()
sys.exit(root.exec_())
