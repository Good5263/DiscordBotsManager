from PyQt5 import QtCore, QtWidgets


class Entrance(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()
        self.customize_elements()
        self.add_layouts()
    
    def create_elements(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 140, 566, 316))
        
        self.login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)

        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        
        self.entrance_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.entrance_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.entrance_label.setAlignment(QtCore.Qt.AlignCenter)

        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_input.setMinimumSize(QtCore.QSize(270, 40))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.login_input.setMinimumSize(QtCore.QSize(270, 40))
        
        self.i_dont_have_account = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.i_dont_have_account.setMinimumSize(QtCore.QSize(270, 45))

        self.entrance_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.entrance_button.setMinimumSize(QtCore.QSize(270, 45))

        self.error_line = QtWidgets.QLineEdit(self)
        self.error_line.setGeometry(QtCore.QRect(20, 530, 317, 50))
        self.error_line.setEnabled(False)
        self.error_line.hide()

    def customize_elements(self):
        self.login_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.i_dont_have_account.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.entrance_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.password_input.setStyleSheet("font: 11pt \"Noto Sans Arabic UI\";")
        self.password_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.login_input.setStyleSheet("font: 11pt \"Noto Sans Arabic UI\";")
        self.entrance_label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.error_line.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")

        self.login_label.setText("Введите логин:")
        self.password_label.setText("Введите пароль:")
        self.entrance_label.setText("Вход")
        self.i_dont_have_account.setText("У меня нет аккаунта")
        self.entrance_button.setText("Войти")
        self.error_line.setText("Неправильный логин или пароль")

    def add_layouts(self):
        self.buttom_layout = QtWidgets.QFormLayout()
        self.buttom_layout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.buttom_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.i_dont_have_account)
        self.buttom_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entrance_button)

        self.main_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.login_label, 2, 0, 1, 1)
        self.main_layout.addLayout(self.buttom_layout, 6, 0, 1, 1)
        self.main_layout.addWidget(self.password_input, 5, 0, 1, 1)
        self.main_layout.addWidget(self.password_label, 4, 0, 1, 1)
        self.main_layout.addWidget(self.login_input, 3, 0, 1, 1)
        self.main_layout.addWidget(self.entrance_label, 1, 0, 1, 1)
