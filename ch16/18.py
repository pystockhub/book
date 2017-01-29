import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 100)

        self.pushButton1= QPushButton("Button1")
        self.pushButton2= QPushButton("Button2")
        self.pushButton3= QPushButton("Button3")

        layout = QHBoxLayout()
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.pushButton3)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
