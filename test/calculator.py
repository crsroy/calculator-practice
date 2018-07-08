import sys
from operation import *
from pushbutton import PushButton
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QApplication, QLineEdit)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.screen = QLineEdit()
        self.bottom = []
        self.text = ''

        # 按钮和位置初始化
        names = ['clear',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i+1,j) for i in range(4) for j in range(4)]
        positions = [(0, 3)] + positions

        grid.setSpacing(10)

        grid.addWidget(self.screen, 0, 0, 1, 3)
        for position, name in zip(positions,names):
            locals()['btn_' + name] = PushButton(name, self)
            locals()['btn_' + name].clicked.connect(self.buttonClicked)
            self.bottom.append(locals()['btn_' + name])
            grid.addWidget(locals()['btn_' + name], *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator by RoyD')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == '=':
            self.output()
        else:
            if sender.text() == 'clear':
                self.text = ''
            else:
                self.text +=  sender.text()
            self.screen.setText(self.text)

    def keyPressEvent(self, event):
        keyEvent = QKeyEvent(event)
        if keyEvent.key() == Qt.Key_Escape:  # Enter键无效，Escape可以表示触发
        #if keyEvent.key() == Qt.Key_Enter:
            self.output()

    def output(self):
        self.text = str_proc(self.text)
        self.screen.setText(str(operation(self.text)))
        self.text = ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
