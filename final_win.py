from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
        self.exp = exp

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_finalwin)
        self.move(win_x, win_y)
    def initUI(self):
        self.main_line = QVBoxLayout()
        self.results = QLabel(txt_index)
        self.comment = QLabel(txt_workheart)
        self.main_line.addWidget(self.results, alignment= Qt.AlignCenter)
        self.main_line.addWidget(self.comment, alignment= Qt.AlignCenter)
        self.setLayout(self.main_line)

# app = QApplication([])
# my_win = FinalWin(2)
# # my_win.set_appear()
# # my_win.initUI()
# # my_win.show()

# app.exec_()