from PyQt5 import QtCore, QtWidgets


class AddBot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()
        self.customize_elements()
        self.add_layouts()
    
    def create_elements(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)

        self.name_bot_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_bot_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.token_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.token_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.name_bot_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.token_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(300, 45))

        self.add_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_bot_button.setMinimumSize(QtCore.QSize(300, 45))

        self.error_line = QtWidgets.QLineEdit(self)
        self.error_line.setGeometry(QtCore.QRect(20, 530, 317, 50))
        self.error_line.setEnabled(False)
        self.error_line.hide()
    
    def customize_elements(self):
        self.name_bot_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.token_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.name_bot_line.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.token_line.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.cancel_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.add_bot_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.error_line.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")

        self.name_bot_label.setText("Название бота:")
        self.token_label.setText("Токен бота:")
        self.cancel_button.setText("В меню")
        self.add_bot_button.setText("Добавить бота")
    
    def add_layouts(self):
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 130, 656, 266))

        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addWidget(self.name_bot_label)
        self.top_layout.addWidget(self.name_bot_line)

        self.medium_layout = QtWidgets.QHBoxLayout()
        self.medium_layout.addWidget(self.token_label)
        self.medium_layout.addWidget(self.token_line)
        
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.addWidget(self.cancel_button)
        self.bottom_layout.addWidget(self.add_bot_button)

        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.medium_layout)
        self.main_layout.addLayout(self.bottom_layout)