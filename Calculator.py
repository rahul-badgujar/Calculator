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

        self.buttons_num=list()
        for i in range(10):
            butt_name='button_'+str(i)
            button=self.window.findChild(QPushButton,butt_name)
            button.released.connect(self.on_buttons_num_released)
            self.buttons_num.append(button)
        
        self.button_dot=self.window.findChild(QPushButton,'button_dot')
        self.button_dot.released.connect(self.on_button_dot_released)

        
        self.button_ac=self.window.findChild(QPushButton,'button_ac')
        self.button_ac.released.connect(self.on_button_ac_released)

        self.button_ac=self.window.findChild(QPushButton,'button_del')
        self.button_ac.released.connect(self.on_button_del_released)

        self.button_ac=self.window.findChild(QPushButton,'button_ans')
        self.button_ac.released.connect(self.on_button_ans_released)

        self.button_ac=self.window.findChild(QPushButton,'button_equal')
        self.button_ac.released.connect(self.on_button_equal_released)

        self.button_ac=self.window.findChild(QPushButton,'button_div')
        self.button_ac.released.connect(self.on_buttons_opr_released)

        self.button_ac=self.window.findChild(QPushButton,'button_mult')
        self.button_ac.released.connect(self.on_buttons_opr_released)

        self.button_ac=self.window.findChild(QPushButton,'button_add')
        self.button_ac.released.connect(self.on_buttons_opr_released)

        self.button_ac=self.window.findChild(QPushButton,'button_sub')
        self.button_ac.released.connect(self.on_buttons_opr_released)

        self.button_ac=self.window.findChild(QPushButton,'button_exp')
        self.button_ac.released.connect(self.on_buttons_opr_released)

        self.display=self.window.findChild(QLabel,'display')
        self.ans_label=self.window.findChild(QLabel,'ans_label')

        self.answer=0.0

        self.active_operator=None

        self.window.show()

    @pyqtSlot()
    def on_button_ac_released(self):
        self.display.setText('0')

    @pyqtSlot()
    def on_buttons_num_released(self):
        button=self.sender()
        if self.display.text()=='0' or self.display.text()=='0.0':
            self.display.setText(button.text())
        else:
            text=self.display.text()
            self.display.setText(text+button.text())

    @pyqtSlot()
    def on_button_dot_released(self):
        text=self.display.text()
        if '.' not in text and text!='':
            self.display.setText(text+'.')

    @pyqtSlot()
    def on_button_del_released(self):
        text=self.display.text()
        if text[0:-1]=='':
            self.display.setText('0')
        else:
            self.display.setText(text[0:-1])

    @pyqtSlot()
    def on_buttons_opr_released(self):
        button=self.sender()
        operator=button.text()
        value=float(self.display.text())

        if self.active_operator==None:
            self.answer=value
        else:
            self.answer=self.operate(value,self.active_operator)

        self.active_operator=operator
        self.ans_label.setText('=  '+str(self.answer)+ ' '+self.active_operator)
        self.display.setText('0')


    @pyqtSlot()
    def on_button_ans_released(self):
        self.display.setText(str(self.answer))

    @pyqtSlot()
    def on_button_equal_released(self):

        value=float(self.display.text())

        if self.active_operator==None:
            self.answer=value
        else:
            self.answer=self.operate(value,self.active_operator)

        self.active_operator=None
        self.ans_label.setText('= '+str(self.answer))
        self.display.setText(str(self.answer))

    def operate(self,value,operator):
        if operator=='+':
            self.answer+=value
        elif operator=='-':
            self.answer-=value
        elif operator=='*':
            self.answer*=value
        elif operator=='/':
            self.answer/=value
        elif operator=='^':
            self.answer=self.answer**value
        return self.answer
        
            


if __name__=='__main__':
    testApp=QApplication(sys.argv)
    calc=Calculator(title='Calculator',parent=None,uiFile='form/ui_calculator.ui')
    testApp.exec_()