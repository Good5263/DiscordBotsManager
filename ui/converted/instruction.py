# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/source/inctruction.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instruction(object):
    def setupUi(self, Instruction):
        Instruction.setObjectName("Instruction")
        Instruction.resize(800, 600)
        self.instruction_box = QtWidgets.QGroupBox(Instruction)
        self.instruction_box.setGeometry(QtCore.QRect(14, 9, 771, 576))
        self.instruction_box.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.instruction_box.setAlignment(QtCore.Qt.AlignCenter)
        self.instruction_box.setObjectName("instruction_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.instruction_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(15, 30, 741, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inctruction_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inctruction_layout.setContentsMargins(0, 0, 0, 0)
        self.inctruction_layout.setSpacing(3)
        self.inctruction_layout.setObjectName("inctruction_layout")
        self.inctruction = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.inctruction.setObjectName("inctruction")
        self.inctruction_layout.addWidget(self.inctruction)
        self.exit_to_menu_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_to_menu_button.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_to_menu_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.exit_to_menu_button.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";")
        self.exit_to_menu_button.setObjectName("exit_to_menu_button")
        self.inctruction_layout.addWidget(self.exit_to_menu_button)

        self.retranslateUi(Instruction)
        QtCore.QMetaObject.connectSlotsByName(Instruction)

    def retranslateUi(self, Instruction):
        _translate = QtCore.QCoreApplication.translate
        Instruction.setWindowTitle(_translate("Instruction", "Form"))
        self.instruction_box.setTitle(_translate("Instruction", "Инструкция"))
        self.exit_to_menu_button.setText(_translate("Instruction", "В меню"))
