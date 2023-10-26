import sys
import random
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class BingoSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initDatabase()
        self.resetGame()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.numberLabel = QLabel('Nextを押して次へ', self)
        self.numberLabel.setAlignment(Qt.AlignCenter)
        self.numberLabel.setFont(QFont('Arial', 200))
        self.layout.addWidget(self.numberLabel)

        self.nextButton = QPushButton('Next', self)
        self.nextButton.clicked.connect(self.nextNumber)
        self.nextButton.setFont(QFont('Arial', 24))
        self.layout.addWidget(self.nextButton)

        self.recordedNumbersText = QTextEdit(self)
        self.recordedNumbersText.setReadOnly(True)
        self.recordedNumbersText.setFont(QFont('Arial', 50))
        self.layout.addWidget(self.recordedNumbersText)

        self.setLayout(self.layout)
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Bingo System')
        self.show()

    def initDatabase(self):
        self.conn = sqlite3.connect('bingo.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS numbers (number INTEGER)')
        self.conn.commit()

    def resetGame(self):
        self.availableNumbers = list(range(1, 76))
        self.recordedNumbers = []
        self.c.execute('DELETE FROM numbers')
        self.conn.commit()
        self.updateRecordedNumbersText()

    def nextNumber(self):
        if not self.availableNumbers:
            self.numberLabel.setText('Game Over!')
            return

        number = random.choice(self.availableNumbers)
        self.availableNumbers.remove(number)
        self.recordedNumbers.append(number)
        self.c.execute('INSERT INTO numbers VALUES (?)', (number,))
        self.conn.commit()
        self.updateRecordedNumbersText()
        self.numberLabel.setText(str(number))

    def updateRecordedNumbersText(self):
        text = ', '.join(map(str, self.recordedNumbers))
        self.recordedNumbersText.setText(text)

def main():
    app = QApplication(sys.argv)
    ex = BingoSystem()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()