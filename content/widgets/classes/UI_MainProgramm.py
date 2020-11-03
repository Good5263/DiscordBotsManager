from PyQt5 import QtCore, QtGui, QtWidgets


class MainProgramm(QtWidgets.QWidget):  # Виджет основного меню
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.create_elements()  # Добавление виджетов
        self.customize_elements()  # Добавление шрифта, текста, картинок в виджеты
        self.add_layouts()  # Добавление виджетов в layout
    
    def create_elements(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(205, 110, 361, 371))

        self.start_bot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_bot_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.help_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.unlogin_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
    
    def customize_elements(self):
        self.start_bot.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.add_bot_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.remove_bot_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.help_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")
        self.unlogin_button.setStyleSheet("font: 10pt \"Noto Sans Arabic UI\";")

        self.start_bot.setText("Запустить бота")
        self.add_bot_button.setText("Добавить бота")
        self.remove_bot_button.setText("Удалить бота")
        self.help_button.setText("Инструкция")
        self.unlogin_button.setText("Выйти из аккаунта")
    
    def add_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.start_bot)
        self.main_layout.addWidget(self.add_bot_button)
        self.main_layout.addWidget(self.remove_bot_button)
        self.main_layout.addWidget(self.help_button)
        self.main_layout.addWidget(self.unlogin_button)
