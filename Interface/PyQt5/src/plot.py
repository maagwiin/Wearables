import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QCategoryAxis, QLineSeries

#### Rascunho

class Plot(QWidget):
    def __init__(self, gas, parent=None):
        super(Plot, self).__init__()
        self.gas = gas
        self.chart = QChart()
        self.series = QLineSeries()
        self.series.append(1, 1)
        self.series.append(2, 2)
        self.series.append(3, 1)
        self.series.append(4, 2)

        self.chart.addSeries(self.series)

        if self.gas == 'A':
            self.chart.setTitle("LPG - History Chart")
        elif self.gas == 'B':
            self.chart.setTitle("CO - History Chart")

        self.chart_view = QChartView(self.chart)
        self.chart_lay = QHBoxLayout()
        self.chart_lay.addWidget(self.chart_view)

        self.setLayout(self.chart_lay)