from PyQt5 import QtCore, QtWidgets


class StartBot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.start_bot_button = QtWidgets.QPushButton(self)
        self.start_bot_button.setGeometry(QtCore.QRect(175, 130, 210, 28))
        self.start_bot_button.setText("Запустить")
        self.start_bot_button.setStyleSheet("font: 9pt \"Arial\";")

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(QtCore.QRect(385, 130, 210, 28))
        self.exit_button.setText("В меню")
        self.exit_button.setStyleSheet("font: 9pt \"Arial\";")

        self.bots = QtWidgets.QComboBox(self)
        self.bots.setGeometry(QtCore.QRect(175, 160, 420, 22))
        self.bots.setStyleSheet("font: 9pt \"Arial\";")
