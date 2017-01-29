import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        label = QLabel("매도수량: ", self)
        label.move(10, 20)

        self.spinBox = QSpinBox(self)
        self.spinBox.move(70, 25)
        self.spinBox.resize(80, 22)
        self.spinBox.valueChanged.connect(self.spinBoxChanged)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def spinBoxChanged(self):
        val = self.spinBox.value()
        msg = '%d 주를 매도합니다.' % (val)
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
