 
from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, name, test1, test2, test3):
        self.age = age
        self.name = name
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
    def initUI(self):
        self.main_line = QHBoxLayout()
        self.first_line = QVBoxLayout()
        self.second_line = QVBoxLayout()

        self.name = QLabel(txt_name)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText(txt_hintname)
        self.name_edit.setStyleSheet("background: white")
        self.age = QLabel(txt_age)
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText(txt_hintage)
        self.age_edit.setStyleSheet("background: white")
        self.instruct = QLabel(txt_starttest1)
        self.start = QPushButton(txt_test1)
        self.start.setStyleSheet("background: white")
        self.result = QLineEdit()
        self.result.setPlaceholderText(txt_hinttest1)
        self.result.setStyleSheet("background: white")

        self.exer_instruct = QLabel(txt_starttest2)
        self.exercise = QPushButton(txt_test2)
        self.exercise.setStyleSheet("background: white")

        self.relax_instruct = QLabel(txt_starttest3)
        self.final_test = QPushButton(txt_test3)
        self.final_test.setStyleSheet("background: white")

        self.now = QLineEdit()
        self.now.setPlaceholderText(txt_hinttest2)
        self.now.setStyleSheet("background: white")
        self.after = QLineEdit()
        self.after.setPlaceholderText(txt_hinttest3)
        self.after.setStyleSheet("background: white")

        self.send_result = QPushButton(txt_sendresults)
        self.send_result.setStyleSheet("background: white")
        self.timer = QLabel(txt_timer)
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("font-size: 50px")
        self.first_line.addWidget(self.name, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.name_edit, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.age, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.age_edit, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.instruct, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.start, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.result, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.exer_instruct, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.exercise, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.relax_instruct, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.final_test, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.now, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.after, alignment= Qt.AlignLeft)
        self.first_line.addWidget(self.send_result, alignment= Qt.AlignCenter)
        self.second_line.addWidget(self.timer, alignment= Qt.AlignCenter)
        
        self.main_line.addLayout(self.first_line)
        self.main_line.addLayout(self.second_line)
        self.setLayout(self.main_line)
    def timer_test1(self):
        global time
        time = QTime(0, 1, 0)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer1Event)
        self.timer1.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("font-size: 50px; color: #8F0037")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer1.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer2Event)
        self.timer1.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss")[6:8])
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("font-size: 50px; color: #8F0037")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer1.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer3Event)
        self.timer1.start(1500)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timer.setStyleSheet("color: #8F0037; font-size: 50px")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer.setStyleSheet("color: #8F0037; font-size: 50px")
        else:
            self.timer.setStyleSheet("color: #519600; font-size: 50px")
        
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer1.stop()
    def next_click(self):
        self.hide()
        global txt_name_final
        exp = Experiment(int(self.age_edit.text()),self.name_edit.text(), int(self.result.text()), int(self.now.text()), int(self.after.text()))
        # print("jjj", self.exp)
        self.tw = FinalWin(exp)
        self.tw.setStyleSheet("background-color: #B5F36D; color: #519600; font-family: Times New Roman; font-size: 30px; margin-bottom:0px")
        print(self.tw)

    def connects(self):
        self.start.clicked.connect(self.timer_test1)
        self.exercise.clicked.connect(self.timer_sits)
        self.final_test.clicked.connect(self.timer_final)
        self.send_result.clicked.connect(self.next_click)

# app = QApplication([])
# my_win = TestWin()
# # my_win.set_appear()
# # my_win.initUI()
# # my_win.connects()
# # my_win.show()

# app.exec_()
 
