import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class Button(QPushButton):
    def __init__(self, text=''):
        super().__init__(text)
        self.setStyleSheet('Font-size: 40px')
    
class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('Font-size: 30px')

class TicTacToe(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.times = 0
        self.turn = '❌'
        self.setWindowTitle('TIC-TAC-TOE')
        self.setFixedSize(330, 440)
        h_b = QHBoxLayout()
        self.restart_btn = Button('↻')
        self.btns = [[Button() for i in range(3)] for j in range(3)]
        self.v_box = QVBoxLayout()
        h_b.addStretch()
        h_b.addWidget(self.restart_btn)
        self.v_box.addLayout(h_b)
        for btns_lst in self.btns:
            h_box = QHBoxLayout()
            for btn in btns_lst:               
                btn.clicked.connect(self.onClick)
                btn.setFixedSize(100, 100)
                h_box.addWidget(btn)
            self.v_box.addLayout(h_box)
        self.label = Label(f'Turn {self.turn}')
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()
        self.v_box.addLayout(h_box)
        self.restart_btn.clicked.connect(self.restart)
        self.setLayout(self.v_box)
        self.show()

    def onClick(self):
        sender = self.sender()
        if not sender.text():
            self.times += 1
            sender.setText(self.turn)
            if self.check() == -1:
                self.label.setText('--- DRAW ---')
                self.deactivate()
            elif self.check():
                self.label.setText(f'WINNER IS {self.turn}')
                self.deactivate()
            else:
                self.turn = '❌' if self.turn == '⭕️' else '⭕️'
                self.label.setText(f'Turn {self.turn}')

    def deactivate(self):
        for i in range(3):
            for j in range(3):
                btn = self.btns[i][j]
                if not btn.text() or btn.text() != self.turn:
                    btn.setEnabled(False)

    def restart(self):
        self.times = 0
        self.turn = '❌'
        self.label.setText(f'Turn {self.turn}')
        for i in range(3):
            for j in range(3):
                self.btns[i][j].setText('')
                self.btns[i][j].setEnabled(True)
                self.btns[i][j].setStyleSheet('font-size: 40px')

    def check(self): 
        style = 'background-color: #13abe5; font-size: 40px'

        if self.times < 5:
            return False
        
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() == self.btns[i][2].text() != '':
                self.btns[i][0].setStyleSheet(style)
                self.btns[i][1].setStyleSheet(style)
                self.btns[i][2].setStyleSheet(style)
                return True
            
            if self.btns[0][i].text() == self.btns[1][i].text() == self.btns[2][i].text() != '':
                self.btns[0][i].setStyleSheet(style)
                self.btns[1][i].setStyleSheet(style)
                self.btns[2][i].setStyleSheet(style)
                return True
            
        if self.btns[0][0].text() == self.btns[1][1].text() == self.btns[2][2].text() != '':
            self.btns[0][0].setStyleSheet(style)
            self.btns[1][1].setStyleSheet(style)
            self.btns[2][2].setStyleSheet(style)
            return True

        if self.btns[2][0].text() == self.btns[1][1].text() == self.btns[0][2].text() != '':
            self.btns[2][0].setStyleSheet(style)
            self.btns[1][1].setStyleSheet(style)
            self.btns[0][2].setStyleSheet(style)
            return True
        
        if self.times == 9:
            return -1

        return False

if __name__ == '__main__':
    app = QApplication([])
    win = TicTacToe()
    sys.exit(app.exec_())