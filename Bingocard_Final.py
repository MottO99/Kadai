import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class BingoCard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.generateCard()
        self.showCard()

        self.newCardButton = QPushButton('New Card', self)
        self.newCardButton.setFont(QFont('Arial', 16))
        self.newCardButton.clicked.connect(self.newCard)
        
        vbox = QVBoxLayout()
        vbox.addLayout(self.grid)
        vbox.addWidget(self.newCardButton)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Bingo Card Generator')
        self.show()

    def generateCard(self):
        self.card = [[0]*5 for _ in range(5)]
        for i in range(5):
            numbers = list(range(i*15 + 1, i*15 + 16))
            for j in range(5):
                self.card[j][i] = str(random.choice(numbers))
                numbers.remove(int(self.card[j][i]))

    def showCard(self):
        for i in range(5):
            for j in range(5):
                label = QLabel(self.card[i][j], self)
                label.setFont(QFont('Arial', 24))
                label.setAlignment(Qt.AlignCenter)
                self.grid.addWidget(label, i, j)

    def newCard(self):
        for i in reversed(range(self.grid.count())): 
            self.grid.itemAt(i).widget().setParent(None)
        self.generateCard()
        self.showCard()

def main():
    app = QApplication(sys.argv)
    ex = BingoCard()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
