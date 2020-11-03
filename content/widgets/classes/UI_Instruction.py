from PyQt5 import QtCore, QtGui, QtWidgets


class Instruction(QtWidgets.QWidget):  # Виджет инструкции
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()  # Добавление виджетов
        self.customize_elements()  # Добавление шрифта, текста, картинок в виджеты

    def create_elements(self):
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(300, 20, 191, 26))

        self.text = QtWidgets.QPlainTextEdit(self)
        self.text.setGeometry(QtCore.QRect(15, 60, 771, 481))

        self.exit = QtWidgets.QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(15, 550, 771, 41))

    def customize_elements(self):
        self.title.setStyleSheet("font: 18pt \"Lucida Console\";")
        self.text.setStyleSheet("font: 16pt \"Lucida Console\";")
        self.exit.setStyleSheet("font: 18pt \"Lucida Console\";")

        self.title.setText("Инструкция")
        self.exit.setText("В главное меню")

        text = open('content/instruction.txt', mode='r', encoding="utf8").read()
        self.text.setPlainText(text)
