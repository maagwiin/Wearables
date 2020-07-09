import sys
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from pyqtgraph import PlotWidget, plot

from random import randint


#### Rascunho
####self.graphWidget.clear()

class Plot(QWidget):
    def __init__(self, gas, parent=None):
        super(Plot, self).__init__()
        self.parent = parent
        self.gas = gas
        self.chart = pg.PlotWidget()
        self.chart.setBackground('w')
        self.chart.setMouseEnabled(x=False, y=False)

        styles = {'color':'p', 'font-size':'15px'}
        self.chart.setLabel('left', 'Concentracao (ppm)', **styles)
        self.chart.showGrid(x=True, y=True)

        self.pen = pg.mkPen(color=(10, 50, 255), width=2)

        self.x = list(range(10))  # 100 time points
        self.y = [randint(0,100) for _ in range(10)]


        self.data_line = self.chart.plot(self.x, self.y, pen=self.pen)
        
        
        self.chart_lay = QHBoxLayout()
        self.chart_lay.addWidget(self.chart)

        self.setLayout(self.chart_lay)




        #if self.gas == 'A':
            #self.chart.setTitle("LPG - History Chart")
        #elif self.gas == 'B':
            #self.chart.setTitle("CO - History Chart")


    def att(self):
        self.x = self.parent.core.index
        self.chart.clear()
        self.data_line = self.chart.plot(self.x, self.y, pen=self.pen)  
        
