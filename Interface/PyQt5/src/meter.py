import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QTextEdit, QComboBox, QGraphicsView, QLabel)

class Meter(QGroupBox):
    def __init__(self, gas, parent=None):
        super(Meter, self).__init__()
        self.parent = parent
        self.gas = gas
        if self.gas == 'A':
            self.name = "  LPG - Liquefied Petroleum Gas  "
        elif self.gas == 'B':
            self.name = "  CO - Carbon Monoxide  "
        
        self.setTitle(self.name)
        self.txt_meter = QLabel()
        self.txt_meter.setStyleSheet(
            '* { background: none; color: red; font-size: 40px; text-align: center;}'
        )

        self.gp_meter_layH = QHBoxLayout()
        self.gp_meter_layV = QVBoxLayout()
        self.gp_meter_layV.addStretch()
        self.gp_meter_layV.addWidget(self.txt_meter)
        self.gp_meter_layV.addStretch()
        self.gp_meter_layH.addStretch()
        self.gp_meter_layH.addLayout(self.gp_meter_layV)
        self.gp_meter_layH.addStretch()
        
        self.setLayout(self.gp_meter_layH)