import sys
from PyQt5.QtWidgets import *

def clicked_slot():
    print("clicked")

app = QApplication(sys.argv)

btn = QPushButton("Hello, PyQt")
btn.clicked.connect(clicked_slot)
btn.show()

app.exec_()