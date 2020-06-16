import sys
from PyQt5.QtWidgets import (QVBoxLayout, QGroupBox, QTextEdit)


class Log(QGroupBox):
    def __init__(self, parent=None):
        super(Log, self).__init__()
        self.setTitle("Log")
        self.txt_log = QTextEdit()
        self.gp_log_lay = QVBoxLayout()
        self.gp_log_lay.addWidget(self.txt_log)
        
        self.setLayout(self.gp_log_lay)


