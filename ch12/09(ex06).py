import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        label = QLabel('종목코드: ', self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
