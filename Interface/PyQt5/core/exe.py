import sys
import random
import time
from datetime import datetime
from PyQt5.QtCore import QTimer

class Exe():
    def __init__(self, parent=None):
        super(Exe, self).__init__()
        self.parent = parent

        self.lpg_current = 0
        self.co_current = 0

        self.lpg_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.co_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.init_log()

        self.timer = QTimer()
        self.timer.timeout.connect(self.push)
        self.timer.start(1000)
        self.parent.com.btn_reset.clicked.connect(self.stop_timer)




    def init_log(self):
        self.ts = time.time()
        self.timestamp = datetime.fromtimestamp(self.ts).strftime('%d/%m/%Y')
        self.parent.log.txt_log.setText("Teste de Logging Wearables - NERA   ---   Data: {}".format(self.timestamp))
        self.parent.log.txt_log.append("Author: Magnu Windell Araujo Santos")
        self.parent.log.txt_log.append("\n")


    def push(self):
        self.lpg_current = random.randrange(100, 1000, 1)
        self.co_current = random.randrange(100, 1000, 1)
        self.att_meter()
        self.att_list()
        self.att_log()


    def att_meter(self):
        self.parent.lpg_meter.txt_meter.setText("{} PPM".format(self.lpg_current))
        self.parent.co_meter.txt_meter.setText("{} PPM".format(self.co_current))

    def att_list(self):
        self.esc = self.lpg_list.pop(0)
        self.lpg_list.append(self.lpg_current)
        self.esc = self.co_list.pop(0)
        self.co_list.append(self.co_current)
        print(self.lpg_list)
        print(self.co_list)
        print("\n")
    
    def att_log(self):
        self.ts = time.time()
        self.timestamp = datetime.fromtimestamp(self.ts).strftime('%H:%M:%S')
        self.parent.log.txt_log.append(self.timestamp + ': LPG: {} PPM --- CO: {} PPM'.format(self.lpg_current, self.co_current))

    def stop_timer(self):
        self.timer.stop()