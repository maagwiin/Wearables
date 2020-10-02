from PyQt5.QtWidgets import QLabel


class Lid(QLabel):
    def __init__(self, parent=None):
        super(Lid, self).__init__()
        self.setText("ID: AA01")
        self.setStyleSheet(
            "font-size: 20px; color: red; padding: 10px"
        )