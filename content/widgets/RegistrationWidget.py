import re
import sqlite3

from PyQt5 import QtWidgets, QtCore
from .classes import Registration, Hash


class RegistrationWidget(Registration):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('content\data.sqlite')
        self.cursor = self.connection.cursor()

        self.symbols = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_')
    
    def validation_account(self):
        login = self.login_line.text()

        password = self.password_line.text()
        password2 = self.password_line2.text()

        login_valid = re.findall(r'[A-Za-z0-9_]', login)
        password_valid = re.findall(r'[A-Za-z0-9_]', password)

        users = self.cursor.execute("SELECT login FROM users").fetchall()

        if len(login_valid) != len(login):
            self.show_error('Логин может состоять только из A-Z a-z 0-9 _')
        elif len(password_valid) != len(password):
            self.show_error('Пароль может состоять только из A-Z a-z 0-9 _')
        elif len(login) < 6:
            self.show_error('Логин меньше 6 символов')
        elif len(login) > 15:
            self.show_error('Логин больше 15 символов')
        elif len(password) < 6:
            self.show_error('Пароль меньше 6 символов')
        elif len(password) > 15:
           self.show_error('Пароль больше 15 символов')
        elif password != password2:
            self.show_error('Пароли не совпадают')
        elif (login,) in users:
            self.show_error('Пользователь с таким логином уже существует')
        else:
            self.error_line.hide()
            
            hash_password = Hash().hash_string(password)

            users = len(self.cursor.execute("SELECT * FROM users").fetchall())
            self.cursor.execute("INSERT INTO users VALUES(?, ?, ?)", (login, hash_password, users + 1))
            self.cursor.execute("INSERT INTO groups VALUES(?, ?)", (users + 1, '0'))

            self.connection.commit()

            return login
        
        return False

    def show_error(self, error):
        self.error_line.setGeometry(QtCore.QRect(20, 530, len(error) * 11, 50))
        self.error_line.setText(error)
        self.error_line.show()
