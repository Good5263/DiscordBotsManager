# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/add_bot.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddBot(object):
    def setupUi(self, AddBot):
        AddBot.setObjectName("AddBot")
        AddBot.resize(800, 600)
        self.list_bots_box = QtWidgets.QGroupBox(AddBot)
        self.list_bots_box.setGeometry(QtCore.QRect(10, 5, 266, 576))
        self.list_bots_box.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.list_bots_box.setAlignment(QtCore.Qt.AlignCenter)
        self.list_bots_box.setObjectName("list_bots_box")
        self.list_bots = QtWidgets.QListWidget(self.list_bots_box)
        self.list_bots.setGeometry(QtCore.QRect(10, 25, 246, 541))
        self.list_bots.setObjectName("list_bots")
        self.add_bot_box = QtWidgets.QGroupBox(AddBot)
        self.add_bot_box.setGeometry(QtCore.QRect(295, 9, 491, 236))
        self.add_bot_box.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.add_bot_box.setAlignment(QtCore.Qt.AlignCenter)
        self.add_bot_box.setObjectName("add_bot_box")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.add_bot_box)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(15, 30, 461, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.form_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(0)
        self.form_layout.setObjectName("form_layout")
        self.name_enter_layout = QtWidgets.QVBoxLayout()
        self.name_enter_layout.setSpacing(0)
        self.name_enter_layout.setObjectName("name_enter_layout")
        self.bot_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.bot_name_label.setMinimumSize(QtCore.QSize(0, 30))
        self.bot_name_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bot_name_label.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.bot_name_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.bot_name_label.setObjectName("bot_name_label")
        self.name_enter_layout.addWidget(self.bot_name_label)
        self.bot_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.bot_name.setMinimumSize(QtCore.QSize(0, 35))
        self.bot_name.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bot_name.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.bot_name.setObjectName("bot_name")
        self.name_enter_layout.addWidget(self.bot_name)
        self.form_layout.addLayout(self.name_enter_layout)
        self.token_enter_layout = QtWidgets.QVBoxLayout()
        self.token_enter_layout.setSpacing(0)
        self.token_enter_layout.setObjectName("token_enter_layout")
        self.bot_token_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.bot_token_label.setMinimumSize(QtCore.QSize(0, 30))
        self.bot_token_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bot_token_label.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.bot_token_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.bot_token_label.setObjectName("bot_token_label")
        self.token_enter_layout.addWidget(self.bot_token_label)
        self.bot_token = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.bot_token.setMinimumSize(QtCore.QSize(0, 35))
        self.bot_token.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bot_token.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.bot_token.setObjectName("bot_token")
        self.token_enter_layout.addWidget(self.bot_token)
        self.form_layout.addLayout(self.token_enter_layout)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setSpacing(3)
        self.buttons_layout.setObjectName("buttons_layout")
        self.exit_to_menu_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.exit_to_menu_button.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_to_menu_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.exit_to_menu_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.exit_to_menu_button.setObjectName("exit_to_menu_button")
        self.buttons_layout.addWidget(self.exit_to_menu_button)
        self.add_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add_bot_button.setMinimumSize(QtCore.QSize(0, 40))
        self.add_bot_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.add_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.add_bot_button.setObjectName("add_bot_button")
        self.buttons_layout.addWidget(self.add_bot_button)
        self.form_layout.addLayout(self.buttons_layout)

        self.retranslateUi(AddBot)
        QtCore.QMetaObject.connectSlotsByName(AddBot)

    def retranslateUi(self, AddBot):
        _translate = QtCore.QCoreApplication.translate
        AddBot.setWindowTitle(_translate("AddBot", "Form"))
        self.list_bots_box.setTitle(_translate("AddBot", "Все боты"))
        self.add_bot_box.setTitle(_translate("AddBot", "Добавление бота"))
        self.bot_name_label.setText(_translate("AddBot", "Название бота:"))
        self.bot_token_label.setText(_translate("AddBot", "Токен бота:"))
        self.exit_to_menu_button.setText(_translate("AddBot", "В меню"))
        self.add_bot_button.setText(_translate("AddBot", "Добавить бота"))
