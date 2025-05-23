 
# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from instr import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def  initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setStyleSheet("color: #519600; font-family: Times New Roman; font-size: 20px; margin-bottom:0px")
        self.instruction = QLabel(txt_instruction)
        self.instruction.setStyleSheet("color: #519600; font-family: Times New Roman; font-size: 15px; text-align: center;")
        self.button = QPushButton(txt_next)
        self.button.setStyleSheet("color: #519600; font-family: Times New Roman; font-size: 15px; background: white")
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)

    def  connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()
        self.tw.setStyleSheet("background-color: #B5F36D; color: #519600; font-family: Times New Roman; font-size: 18px; margin-bottom:0px")

STYLE = '''
QPushButton {
    outline: none;
    border: 1px solid #519600;
    padding: 5px;
    border-radius: 5px;
    text-transform: uppercase;
    background: white;
    color: #519600;
    font-family: Times New Roman;
    font-size: 15px;
}
QLineEdit {
    outline: none;
    border: 1px solid #519600;
    padding: 5px;
    border-radius: 5px;
}
}
'''
app = QApplication([])
app.setStyleSheet(STYLE)
mw = MainWin()
mw.setStyleSheet("background-color: #B5F36D;")
app.exec_()
 

