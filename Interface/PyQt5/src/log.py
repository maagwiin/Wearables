from PyQt5.QtWidgets import (QVBoxLayout, QGroupBox, QTextEdit)
from PyQt5.QtCore import Qt

class Log(QGroupBox):
    def __init__(self, parent=None):
        super(Log, self).__init__()
        self.setTitle("  Log  ")
        self.txt_log = QTextEdit()
        self.gp_log_lay = QVBoxLayout()
        self.gp_log_lay.addWidget(self.txt_log)
        #self.txt_log.setDisabled(True)
        #self.txt_log.setStyleSheet(
        #    '* { background: white; color: black; font-size: 12px;}'
        #)
        self.txt_log.setTextInteractionFlags(Qt.TextBrowserInteraction)


        self.setLayout(self.gp_log_lay)


