import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QComboBox)

class Com(QWidget):
    def __init__(self, parent=None):
        super(Com, self).__init__()
        self.parent = parent
        self.create_widgets()
        self.set_layout()
    
    def create_widgets(self):
        self.select_com = QPushButton("Change", self)
        self.btn_conn = QPushButton("Connect", self)
        self.btn_save = QPushButton("Save Log", self)
        self.btn_reset = QPushButton("Reset", self)

    def set_layout(self):
        self.com_layout = QHBoxLayout()
        self.com_layout.addWidget(self.select_com)
        self.com_layout.addWidget(self.btn_conn)
        self.com_layout.addWidget(self.btn_save)
        self.com_layout.addWidget(self.btn_reset)
        
        self.setLayout(self.com_layout)


