import sys
import os
import random
import time
from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog

class Exe():
    def __init__(self, parent=None):
        super(Exe, self).__init__()
        self.parent = parent
        self.timer = QTimer()

        self.start()

        self.parent.com.btn_conn.clicked.connect(self.ar_connect)
        self.parent.com.btn_save.clicked.connect(self.save_log)
        self.parent.com.btn_reset.clicked.connect(self.reset_system)
        self.timer.timeout.connect(self.push)



    def start(self):
        self.lpg_current = 0
        self.co_current = 0
        self.lpg_list = [0]*30
        self.co_list = [0]*30
        self.index = list(range(30))
        self.init_log()
        self.init_plot()
        self.parent.com.btn_conn.setDisabled(False)
        self.parent.com.btn_save.setDisabled(True)
        


    def init_log(self):
        self.ts = time.time()
        self.timestamp = datetime.fromtimestamp(self.ts).strftime('%d/%m/%Y')
        self.parent.log.txt_log.setText("Log Wearables - NERA   ---   Data: {}".format(self.timestamp))
        self.parent.log.txt_log.append("Autor: Magnu Windell Araujo Santos")
        self.parent.log.txt_log.append("\n")



    def init_plot(self):
        self.parent.lpg_plot.chart.clear()
        self.parent.co_plot.chart.clear()
        self.parent.lpg_plot.x = self.index
        self.parent.co_plot.x = self.index
        self.parent.lpg_plot.y = self.lpg_list
        self.parent.co_plot.y = self.co_list



    def push(self):
        self.lpg_current = random.randrange(100, 1000, 1)
        self.co_current = random.randrange(100, 1000, 1)


        self.att_meter()
        self.att_list()
        self.att_plot()
        self.att_log()


    def att_meter(self):
        self.parent.lpg_meter.txt_meter.setText("{} PPM".format(self.lpg_current))
        self.parent.co_meter.txt_meter.setText("{} PPM".format(self.co_current))



    def att_list(self):
        self.index = self.index[1:]
        self.index.append(self.index[-1] + 1)

        self.lpg_list = self.lpg_list[1:]
        self.lpg_list.append(self.lpg_current)
        self.co_list = self.co_list[1:]
        self.co_list.append(self.co_current)
    

    def att_plot(self):
        self.parent.lpg_plot.y = self.lpg_list
        self.parent.co_plot.y = self.co_list
        self.parent.lpg_plot.att()
        self.parent.co_plot.att()

   


    def att_log(self):
        self.ts = time.time()
        self.timestamp = datetime.fromtimestamp(self.ts).strftime('| %H:%M:%S |  ')
        self.parent.log.txt_log.append(self.timestamp + 'LPG: {} PPM --- CO: {} PPM'.format(self.lpg_current, self.co_current))




    def ar_connect(self):
        self.init_log()
        self.parent.log.txt_log.append('Iniciando Registros...\n')
        self.timer.start(1000)
        self.parent.com.btn_conn.setDisabled(True)
        self.parent.com.btn_save.setDisabled(False)



    def save_log(self):
        self.timer.stop()
        self.ts = time.time()
        self.timestamp = datetime.fromtimestamp(self.ts).strftime(' %d/%m/%Y às %H:%M:%S ')
        self.parent.log.txt_log.append("\nRegistro finalizado em "+ self.timestamp)
        self.filename = QFileDialog.getSaveFileName(self.parent, 'Salvar Log', os.getenv('HOME'))
        try:
            with open(self.filename[0], 'w') as f:
                self.my_log = self.parent.log.txt_log.toPlainText()
                f.write(self.my_log)
        except:
            pass
        



    def reset_system(self):
        self.timer.stop()
        self.parent.lpg_meter.txt_meter.setText("--- PPM")
        self.parent.co_meter.txt_meter.setText("--- PPM")
        self.start()
