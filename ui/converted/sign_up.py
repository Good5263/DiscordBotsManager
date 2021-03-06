# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignUp.sizePolicy().hasHeightForWidth())
        SignUp.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(SignUp)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(95, 125, 601, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.form_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(4)
        self.form_layout.setObjectName("form_layout")
        self.enter_login_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.enter_login_label.setMinimumSize(QtCore.QSize(0, 50))
        self.enter_login_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.enter_login_label.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.enter_login_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.enter_login_label.setObjectName("enter_login_label")
        self.form_layout.addWidget(self.enter_login_label)
        self.login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login.setMinimumSize(QtCore.QSize(0, 40))
        self.login.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.login.setObjectName("login")
        self.form_layout.addWidget(self.login)
        self.enter_password_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.enter_password_label.setMinimumSize(QtCore.QSize(0, 50))
        self.enter_password_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.enter_password_label.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.enter_password_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.enter_password_label.setObjectName("enter_password_label")
        self.form_layout.addWidget(self.enter_password_label)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setMinimumSize(QtCore.QSize(0, 40))
        self.password.setStyleSheet("font: 63 6pt \"Yu Gothic UI Semibold\";")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.form_layout.addWidget(self.password)
        self.repeat_password_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.repeat_password_label.setMinimumSize(QtCore.QSize(0, 50))
        self.repeat_password_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.repeat_password_label.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.repeat_password_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.repeat_password_label.setObjectName("repeat_password_label")
        self.form_layout.addWidget(self.repeat_password_label)
        self.repeat_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.repeat_password.setMinimumSize(QtCore.QSize(0, 40))
        self.repeat_password.setStyleSheet("font: 63 6pt \"Yu Gothic UI Semibold\";")
        self.repeat_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeat_password.setObjectName("repeat_password")
        self.form_layout.addWidget(self.repeat_password)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.i_have_accont = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.i_have_accont.setMinimumSize(QtCore.QSize(0, 45))
        self.i_have_accont.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.i_have_accont.setObjectName("i_have_accont")
        self.buttons_layout.addWidget(self.i_have_accont)
        self.sign_up_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sign_up_button.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_up_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.sign_up_button.setObjectName("sign_up_button")
        self.buttons_layout.addWidget(self.sign_up_button)
        self.form_layout.addLayout(self.buttons_layout)
        self.sign_up_label = QtWidgets.QLabel(SignUp)
        self.sign_up_label.setGeometry(QtCore.QRect(245, 80, 281, 56))
        self.sign_up_label.setStyleSheet("font: 63 18pt \"Yu Gothic UI Semibold\";")
        self.sign_up_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_up_label.setObjectName("sign_up_label")
        self.error_line = QtWidgets.QLineEdit(SignUp)
        self.error_line.setEnabled(False)
        self.error_line.setGeometry(QtCore.QRect(17, 550, 106, 36))
        self.error_line.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";")
        self.error_line.setAlignment(QtCore.Qt.AlignCenter)
        self.error_line.setObjectName("error_line")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Form"))
        self.enter_login_label.setText(_translate("SignUp", "Введите логин:"))
        self.enter_password_label.setText(_translate("SignUp", "Введите пароль:"))
        self.repeat_password_label.setText(_translate("SignUp", "Введите пароль еще раз:"))
        self.i_have_accont.setText(_translate("SignUp", "У меня уже есть аккаунт"))
        self.sign_up_button.setText(_translate("SignUp", "Зарегистрироваться"))
        self.sign_up_label.setText(_translate("SignUp", "Регистрация"))
