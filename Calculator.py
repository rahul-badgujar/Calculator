import sys
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Calculator(QMainWindow):
    def __init__(self,title='Calculator',parent=None,uiFile=None):
        super(Calculator,self).__init__(parent)
        self.window=QMainWindow()
        self.window.setWindowTitle('Calculator App : Made by Rahul')
        loadUi(uiFile,self.window)
        
        self.button_ac=self.window.findChild(QPushButton,'button_ac')
        self.button_ac.released.connect(self.on_button_ac_released)

        self.display=self.window.findChild(QLineEdit,'display')

        self.window.show()

    def on_button_ac_released(self):
        self.display.setText('')

if __name__=='__main__':
    testApp=QApplication(sys.argv)
    calc=Calculator(title='Calculator',parent=None,uiFile='form/ui_calculator.ui')
    testApp.exec_()