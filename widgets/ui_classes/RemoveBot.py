from PyQt5 import QtCore, QtGui, QtWidgets


class RemoveBot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()
        self.customize_elements()
    
    def create_elements(self):
        self.all_bots_label = QtWidgets.QLabel(self)
        self.all_bots_label.setGeometry(QtCore.QRect(15, 10, 119, 26))
        self.all_bots_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.name_bot_label = QtWidgets.QLabel(self)
        self.name_bot_label.setGeometry(QtCore.QRect(320, 15, 236, 26))
        self.name_bot_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.all_bots_list = QtWidgets.QListWidget(self)
        self.all_bots_list.setGeometry(QtCore.QRect(15, 40, 276, 551))

        self.name_bot_line = QtWidgets.QLineEdit(self)
        self.name_bot_line.setGeometry(QtCore.QRect(320, 45, 290, 30))
        self.name_bot_line.setMinimumSize(QtCore.QSize(400, 30))
        self.name_bot_line.setReadOnly(True)

        self.remove_bot_button = QtWidgets.QPushButton(self)
        self.remove_bot_button.setGeometry(QtCore.QRect(530, 90, 200, 45))
        self.remove_bot_button.setMinimumSize(QtCore.QSize(200, 45))
        
        self.cancel_button = QtWidgets.QPushButton(self)
        self.cancel_button.setGeometry(QtCore.QRect(320, 90, 200, 45))
        self.cancel_button.setMinimumSize(QtCore.QSize(200, 45))
    
    def customize_elements(self):
        self.remove_bot_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.all_bots_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.name_bot_line.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.name_bot_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.cancel_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")

        self.all_bots_label.setText("Все боты:")
        self.name_bot_label.setText("Удаляемый бот:")
        self.remove_bot_button.setText("Удалить бота")
        self.cancel_button.setText("В меню")
