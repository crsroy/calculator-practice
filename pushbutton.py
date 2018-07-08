from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class PushButton(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.init_button()

    def init_button(self,):
        self.resize(40, 40)
        self.setFont(QFont('Timers', 10))
