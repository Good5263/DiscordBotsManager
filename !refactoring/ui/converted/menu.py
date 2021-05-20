# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 149, 366, 306))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttons_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setObjectName("buttons_layout")
        self.start_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_bot_button.setMinimumSize(QtCore.QSize(0, 50))
        self.start_bot_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.start_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.start_bot_button.setObjectName("start_bot_button")
        self.buttons_layout.addWidget(self.start_bot_button)
        self.add_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_bot_button.setMinimumSize(QtCore.QSize(0, 50))
        self.add_bot_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.add_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.add_bot_button.setObjectName("add_bot_button")
        self.buttons_layout.addWidget(self.add_bot_button)
        self.remove_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_bot_button.setMinimumSize(QtCore.QSize(0, 50))
        self.remove_bot_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.remove_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.remove_bot_button.setObjectName("remove_bot_button")
        self.buttons_layout.addWidget(self.remove_bot_button)
        self.show_instruction_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_instruction_button.setMinimumSize(QtCore.QSize(0, 50))
        self.show_instruction_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.show_instruction_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.show_instruction_button.setObjectName("show_instruction_button")
        self.buttons_layout.addWidget(self.show_instruction_button)
        self.logout_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logout_button.setMinimumSize(QtCore.QSize(0, 50))
        self.logout_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.logout_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.logout_button.setObjectName("logout_button")
        self.buttons_layout.addWidget(self.logout_button)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.start_bot_button.setText(_translate("Menu", "Запустить бота"))
        self.add_bot_button.setText(_translate("Menu", "Добавить бота"))
        self.remove_bot_button.setText(_translate("Menu", "Удалить бота"))
        self.show_instruction_button.setText(_translate("Menu", "Инструкция"))
        self.logout_button.setText(_translate("Menu", "Выйти из аккаунта"))
