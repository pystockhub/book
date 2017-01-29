import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        groupBox = QGroupBox("시간 단위", self)
        groupBox.move(10, 10)
        groupBox.resize(280, 80)

        self.radio1 = QRadioButton("일봉", self)
        self.radio1.move(20, 20)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("주봉", self)
        self.radio2.move(20, 40)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton("월봉", self)
        self.radio3.move(20, 60)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def radioButtonClicked(self):
        msg = ""
        if self.radio1.isChecked():
            msg = "일봉"
        elif self.radio2.isChecked():
            msg = "주봉"
        else:
            msg = "월봉"
        self.statusBar.showMessage(msg + "선택 됨")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
