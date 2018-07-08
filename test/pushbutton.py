import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont


class PushButton(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.init_button()

    def init_button(self,):
        self.resize(40, 40)
        self.setFont(QFont('Timers',10))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = QWidget()
    frame.setGeometry(400, 400, 300, 260)
    frame.setWindowTitle('xxxxxx')
    button = PushButton('XXX', frame)
    button.move(100, 100)
    frame.show()
    sys.exit(app.exec())