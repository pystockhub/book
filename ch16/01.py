import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello, PyQt")
label.show()

print("Before event loop")
app.exec_()
print("After event loop")
