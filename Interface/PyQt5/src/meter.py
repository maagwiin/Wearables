import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QTextEdit, QComboBox, QGraphicsView)

class Meter(QGroupBox):
    def __init__(self, gas, parent=None):
        super(Meter, self).__init__()
        self.gas = gas
        if self.gas == 'A':
            self.name = "LPG - Liquefied Petroleum Gas"
        elif self.gas == 'B':
            self.name = "CO - Carbon Monoxide"
        
        self.setTitle(self.name)
        self.txt_meter = QTextEdit()
        self.gp_meter_lay = QVBoxLayout()
        self.gp_meter_lay.addWidget(self.txt_meter)
        
        self.setLayout(self.gp_meter_lay)