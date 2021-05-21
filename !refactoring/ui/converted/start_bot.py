# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/start_bot.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartBot(object):
    def setupUi(self, StartBot):
        StartBot.setObjectName("StartBot")
        StartBot.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(StartBot)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 80, 586, 96))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setSpacing(3)
        self.v_layout.setObjectName("v_layout")
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setSpacing(3)
        self.buttons_layout.setObjectName("buttons_layout")
        self.exit_to_menu_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_to_menu_button.setMinimumSize(QtCore.QSize(0, 45))
        self.exit_to_menu_button.setMaximumSize(QtCore.QSize(16777215, 45))
        self.exit_to_menu_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.exit_to_menu_button.setObjectName("exit_to_menu_button")
        self.buttons_layout.addWidget(self.exit_to_menu_button)
        self.start_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_bot_button.setMinimumSize(QtCore.QSize(0, 45))
        self.start_bot_button.setMaximumSize(QtCore.QSize(16777215, 45))
        self.start_bot_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.start_bot_button.setObjectName("start_bot_button")
        self.buttons_layout.addWidget(self.start_bot_button)
        self.v_layout.addLayout(self.buttons_layout)
        self.list_bots = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.list_bots.setMinimumSize(QtCore.QSize(0, 40))
        self.list_bots.setMaximumSize(QtCore.QSize(16777215, 40))
        self.list_bots.setObjectName("list_bots")
        self.v_layout.addWidget(self.list_bots)

        self.retranslateUi(StartBot)
        QtCore.QMetaObject.connectSlotsByName(StartBot)

    def retranslateUi(self, StartBot):
        _translate = QtCore.QCoreApplication.translate
        StartBot.setWindowTitle(_translate("StartBot", "Form"))
        self.exit_to_menu_button.setText(_translate("StartBot", "В меню"))
        self.start_bot_button.setText(_translate("StartBot", "Запустить"))
