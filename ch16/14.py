import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)
        self.setTableWidgetData()

    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
