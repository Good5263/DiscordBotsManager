import sqlite3

from PyQt5 import QtWidgets
from .classes import Entrance, Hash


class EntranceWidget(Entrance):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('content\data.sqlite')
        self.cursor = self.connection.cursor()
    
    def validation_account(self):
        self.error_line.hide()

        login = self.login_input.text()
        password = self.password_input.text()

        users = self.cursor.execute("SELECT * FROM users").fetchall()
        users = [[user[0], user[1]] for user in users]

        if [login, Hash().hash_string(password)] in users:
            return login
        else:
            self.error_line.show()
            return False
