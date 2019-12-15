import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from Calculator import Calculator

app=QApplication(sys.argv)
calculator=Calculator(title='Calculator',parent=None,uiFile='form/ui_calculator.ui')
app.exec_()