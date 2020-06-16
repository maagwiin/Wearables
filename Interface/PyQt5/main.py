import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QTextEdit, QComboBox, QGraphicsView)
from PyQt5.QtGui import QIcon
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QCategoryAxis, QLineSeries
from src.com import Com

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.settings()
        self.create_widgets()
        self.set_layout()
    
    def settings(self):
        self.setWindowTitle("Interface De Monitoramento - Wearables Gases - NERA")
        self.setWindowIcon(QIcon("./static/icon.svg"))
        self.setFixedSize(1200, 700)
    
    def create_widgets(self):
        self.label_id = QLabel()
        self.label_id.setText("ID: AA01")
        self.label_id.setStyleSheet(
            "font-size: 20px; color: red; padding: 10px"
        )

        self.com = Com(self)

        self.gp_log = QGroupBox("Log")
        self.gp_log_lay = QVBoxLayout()
        self.txt_log = QTextEdit()
        self.gp_log_lay.addWidget(self.txt_log)


        self.create_charts()
    
    def create_charts(self):
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



    def set_layout(self):
        
        self.gp_log.setLayout(self.gp_log_lay)

        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.label_id, 0, 0, 1, 2)
        self.main_layout.addWidget(self.com, 1, 0, 1, 2)
        self.main_layout.addWidget(self.gp_log, 2, 0, 2, 1)
        self.main_layout.addWidget(self.lpg_chart_view, 2, 1, 1, 1)
        self.main_layout.addWidget(self.co_chart_view, 3, 1, 1, 1)
        self.setLayout(self.main_layout)


root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
