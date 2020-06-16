import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QCategoryAxis, QLineSeries

#### Rascunho

class Plot(QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__()
        self.lpg_chart = QChart()
        self.lpg_series = QLineSeries()
        self.lpg_series.append(1, 1)
        self.lpg_series.append(2, 2)
        self.lpg_series.append(3, 1)
        self.lpg_series.append(4, 2)

        self.lpg_chart.addSeries(self.lpg_series)
        self.lpg_chart.setTitle("LPG - History Chart")

        self.lpg_chart_view = QChartView(self.lpg_chart)


        self.co_chart = QChart()
        self.co_series = QLineSeries()
        self.co_series.append(1, 1)
        self.co_series.append(2, 2)
        self.co_series.append(3, 1)
        self.co_series.append(4, 2)

        self.co_chart.addSeries(self.co_series)
        self.co_chart.setTitle("CO - History Chart")

        self.co_chart_view = QChartView(self.co_chart)
