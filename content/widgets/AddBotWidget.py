import sqlite3

from PyQt5 import QtWidgets, QtCore
from .classes import AddBot


class AddBotWidget(AddBot):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('content\data.sqlite')
        self.cursor = self.connection.cursor()
    
    def add_bot(self):
        name_bot = self.name_bot_line.text()
        token = self.token_line.text()

        if token == '' or token.isspace() or name_bot == '' or name_bot.isspace():
            self.show_error('Поля токена и названия бота должны быть заполнены')
            return False
    
        bots = self.cursor.execute("SELECT name_bot FROM bots").fetchall()
        if (name_bot,) in bots:
            self.show_error('Бот с таким названием уже есть')
            return False

        try:
            all_entry = self.cursor.execute("SELECT * FROM bots").fetchall()
            last_id = all_entry[-1][0] + 1
        except:
            last_id = 1

        self.cursor.execute("INSERT INTO bots VALUES(?, ?, ?)", (last_id, name_bot, token))
        self.connection.commit()

        return last_id
    
    def show_error(self, error):
        self.error_line.setGeometry(QtCore.QRect(20, 530, len(error) * 11, 50))
        self.error_line.setText(error)
        self.error_line.show()
    