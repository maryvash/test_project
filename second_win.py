from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
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
        self.name_edit = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.age_edit = QLineEdit(txt_hintage)
        self.instruct = QLabel(txt_starttest1)
        self.start = QPushButton(txt_test1)
        self.result = QLineEdit(txt_hinttest1)

        self.exer_instruct = QLabel(txt_starttest2)
        self.exercise = QPushButton(txt_test2)

        self.relax_instruct = QLabel(txt_starttest3)
        self.final_test = QPushButton(txt_test3)

        self.now = QLineEdit(txt_hinttest2)
        self.after = QLineEdit(txt_hinttest3)

        self.send_result = QPushButton(txt_sendresults)
        self.timer = QLabel(txt_timer)
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("color: rgb(0, 0, 0)")
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
        self.second_line.addWidget(self.timer, alignment= Qt.AlignRight)
        
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
        self.timer.setStyleSheet("color: rgb(0, 0, 0)")
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
        self.timer.setStyleSheet("color: rgb(0, 0, 0)")
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
            self.timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.timer.setStyleSheet("color: rgb(0, 0, 0)")
        
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer1.stop()
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.age_edit.text(), self.result.text(), self.now.text(), self.after.text())
        self.tw = FinalWin(self.exp)
    def connects(self):
        self.start.clicked.connect(self.timer_test1)
        self.exercise.clicked.connect(self.timer_sits)
        self.final_test.clicked.connect(self.timer_final)
        self.send_result.clicked.connect(self.next_click)

app = QApplication([])
my_win = TestWin()
# my_win.set_appear()
# my_win.initUI()
# my_win.connects()
# my_win.show()

app.exec_()