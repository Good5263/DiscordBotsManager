# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/remove_bot.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoveBot(object):
    def setupUi(self, RemoveBot):
        RemoveBot.setObjectName("RemoveBot")
        RemoveBot.resize(800, 600)
        self.list_bots_box = QtWidgets.QGroupBox(RemoveBot)
        self.list_bots_box.setGeometry(QtCore.QRect(15, 10, 266, 576))
        self.list_bots_box.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.list_bots_box.setAlignment(QtCore.Qt.AlignCenter)
        self.list_bots_box.setObjectName("list_bots_box")
        self.list_bots = QtWidgets.QListWidget(self.list_bots_box)
        self.list_bots.setGeometry(QtCore.QRect(10, 25, 246, 541))
        self.list_bots.setObjectName("list_bots")
        self.remove_bot_box = QtWidgets.QGroupBox(RemoveBot)
        self.remove_bot_box.setGeometry(QtCore.QRect(300, 9, 486, 131))
        self.remove_bot_box.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.remove_bot_box.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_bot_box.setObjectName("remove_bot_box")
        self.remove_bot_info = QtWidgets.QLineEdit(self.remove_bot_box)
        self.remove_bot_info.setGeometry(QtCore.QRect(10, 25, 466, 36))
        self.remove_bot_info.setReadOnly(True)
        self.remove_bot_info.setObjectName("remove_bot_info")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.remove_bot_box)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 466, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setSpacing(3)
        self.buttons_layout.setObjectName("buttons_layout")
        self.exit_to_menu_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exit_to_menu_button.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_to_menu_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.exit_to_menu_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.exit_to_menu_button.setObjectName("exit_to_menu_button")
        self.buttons_layout.addWidget(self.exit_to_menu_button)
        self.remove_bot_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.remove_bot_button.setMinimumSize(QtCore.QSize(0, 40))
        self.remove_bot_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.remove_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.remove_bot_button.setObjectName("remove_bot_button")
        self.buttons_layout.addWidget(self.remove_bot_button)

        self.retranslateUi(RemoveBot)
        QtCore.QMetaObject.connectSlotsByName(RemoveBot)

    def retranslateUi(self, RemoveBot):
        _translate = QtCore.QCoreApplication.translate
        RemoveBot.setWindowTitle(_translate("RemoveBot", "Form"))
        self.list_bots_box.setTitle(_translate("RemoveBot", "Все боты"))
        self.remove_bot_box.setTitle(_translate("RemoveBot", "Удаляемый бот"))
        self.exit_to_menu_button.setText(_translate("RemoveBot", "В меню"))
        self.remove_bot_button.setText(_translate("RemoveBot", "Удалить бота"))
