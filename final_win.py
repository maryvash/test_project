# напиши здесь код третьего экрана приложения


from instr import *
# from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.exp = exp
        self.initUI()
        self.show()


    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_finalwin)
        self.move(win_x, win_y)
        
        
    def results (self):
        self.index=(4*(int(self.exp.test1)+int(self.exp.test2)+int(self.exp.test3))-200)/10
        if int(self.exp.age) >= 15:
            if int(self.index) >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<=0.4:
                return txt_res5
        elif self.exp.age >= 13 and self.exp.age <=14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.5 and self.index>=12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            elif self.index<=1.9:
                return txt_res5
        elif self.exp.age >= 11 and self.exp.age <=12:
            if self.index >= 18:
                return txt_res1
            elif self.index<17.9 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            elif self.index<=3.4:
                return txt_res5    
        elif self.exp.age >= 9 and self.exp.age <=10:
            if self.index >=19.5:
                return txt_res1
            elif self.index<19.4 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            elif self.index<=4.9:
                return txt_res5
        elif self.exp.age >=7 and self.exp.age <=8:
            if self.index >=21:
                return txt_res1
            elif self.index<20.9 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            elif self.index<=6.4:
                return txt_res5     
    def initUI(self):
        self.main_line = QVBoxLayout()
        self.work_text = QLabel(txt_workheart+self.results())
        self.name_result = QLabel(self.exp.name + ", " + "твои результаты:")
        self.index_text = QLabel(txt_index + str(self.index))
        self.main_line.addWidget(self.name_result, alignment= Qt.AlignCenter)
        self.main_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.main_line.addWidget(self.work_text, alignment= Qt.AlignCenter)
        self.setLayout(self.main_line)
 


 

# app = QApplication([])
# my_win = FinalWin(2)
# my_win.set_appear()
# my_win.initUI()
# my_win.show()

# app.exec_()
 
