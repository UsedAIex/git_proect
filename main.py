import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.Chircle)
        self.painter = None

    def Chircle(self):
        self.painter = True
        self.repaint()

    def paintEvent(self, event):
        if self.painter:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.painter = False

    def draw(self, qp):
        qp.setBrush(QColor(255, 238, 105))
        b = randint(1, 251)
        qp.drawEllipse(250, 150, b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ppa = Program()
    ppa.show()
    sys.exit(app.exec())