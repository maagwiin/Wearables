import sys
import random
from PyQt5.QtCore import QTimer

class Exe():
    def __init__(self, parent=None):
        super(Exe, self).__init__()
        self.parent = parent
        self.lpg_current = 0
        self.co_current = 0
        self.push()
        self.att_meter()
        self.timer = QTimer()
        self.timer.timeout.connect(self.push)
        self.timer.start(100)

    def push(self):
        self.lpg_current = random.randrange(100, 1000, 1)
        self.co_current = random.randrange(100, 1000, 1)
        self.att_meter()

    def att_meter(self):
        self.parent.lpg_meter.txt_meter.setText("{} PPM".format(self.lpg_current))
        self.parent.co_meter.txt_meter.setText("{} PPM".format(self.co_current))