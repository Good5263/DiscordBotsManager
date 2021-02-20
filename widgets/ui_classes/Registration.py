from PyQt5 import QtCore, QtWidgets


class Registration(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()
        self.customize_elements()
        self.add_layouts()
    
    def create_elements(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 65, 566, 421))

        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)

        self.password_label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)

        self.regestration_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.regestration_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.regestration_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)

        self.login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)

        self.password_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_line.setMinimumSize(QtCore.QSize(270, 40))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password_line2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_line2.setMinimumSize(QtCore.QSize(270, 40))
        self.password_line2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.login_line.setMinimumSize(QtCore.QSize(270, 40))
        
        self.registation_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.registation_button.setMinimumSize(QtCore.QSize(270, 45))

        self.i_have_account = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.i_have_account.setMinimumSize(QtCore.QSize(270, 45))

        self.error_line = QtWidgets.QLineEdit(self)
        self.error_line.setGeometry(QtCore.QRect(20, 530, 317, 50))
        self.error_line.setEnabled(False)
        self.error_line.hide()

    def customize_elements(self):
        self.password_label2.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.login_line.setStyleSheet("font: 11pt \"Noto Sans Arabic UI\";")
        self.password_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.regestration_label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.password_line2.setStyleSheet("font: 11pt \"Noto Sans Arabic UI\";")
        self.login_label.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.password_line.setStyleSheet("font: 11pt \"Noto Sans Arabic UI\";")
        self.registation_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.i_have_account.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.error_line.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")

        self.password_label2.setText("Введите пароль ещё раз:")
        self.password_label.setText("Введите пароль:")
        self.regestration_label.setText("Регистрация")
        self.login_label.setText("Введите логин:")
        self.registation_button.setText("Зарегистрироваться")
        self.i_have_account.setText("У меня уже есть аккаунт")
    
    def add_layouts(self):
        self.buttom_layout = QtWidgets.QFormLayout()
        self.buttom_layout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.buttom_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registation_button)
        self.buttom_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.i_have_account)

        self.main_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.password_label2, 5, 0, 1, 1)
        self.main_layout.addWidget(self.login_line, 2, 0, 1, 1)
        self.main_layout.addWidget(self.password_label, 3, 0, 1, 1)
        self.main_layout.addWidget(self.regestration_label, 0, 0, 1, 1)
        self.main_layout.addWidget(self.password_line2, 6, 0, 1, 1)
        self.main_layout.addWidget(self.login_label, 1, 0, 1, 1)
        self.main_layout.addWidget(self.password_line, 4, 0, 1, 1)
        self.main_layout.addLayout(self.buttom_layout, 7, 0, 1, 1)
