import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 500, 300)

        groupBox = QGroupBox("검색옵션")
        checkBox1 = QCheckBox("상한가")
        checkBox2 = QCheckBox("하한가")
        checkBox3 = QCheckBox("시가총액 상위")
        checkBox4 = QCheckBox("시가총액 하위")
        checkBox5 = QCheckBox("회전율 상위")
        checkBox6 = QCheckBox("대량거래상위")
        checkBox7 = QCheckBox("환산주가상위")
        checkBox8 = QCheckBox("외국인한도소진상위")
        checkBox9 = QCheckBox("투자자별순위")

        tableWidget = QTableWidget(10, 5)
        tableWidget.setHorizontalHeaderLabels(["종목코드", "종목명", "현재가", "등락률", "거래량"])
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(checkBox1)
        leftInnerLayOut.addWidget(checkBox2)
        leftInnerLayOut.addWidget(checkBox3)
        leftInnerLayOut.addWidget(checkBox4)
        leftInnerLayOut.addWidget(checkBox5)
        leftInnerLayOut.addWidget(checkBox6)
        leftInnerLayOut.addWidget(checkBox7)
        leftInnerLayOut.addWidget(checkBox8)
        leftInnerLayOut.addWidget(checkBox9)
        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(tableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
