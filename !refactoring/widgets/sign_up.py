import re
import sqlite3
import hashlib

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from ui.converted import SignUpInterface


class SignUpWidget(QWidget, SignUpInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.error_line.hide()

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

    def validation_account(self):
        login = self.login.text()
        password = self.password.text()
        repeat_password = self.repeat_password.text()

        correct_login = "".join(re.findall(r"[A-Za-z0-9_]", login))
        correct_password = "".join(re.findall(r"[A-Za-z0-9_]", password))

        if correct_login != login:
            self.show_error("Логин может состоять только из A-Z a-z 0-9 _")
        elif correct_password != password:
            self.show_error("Пароль может состоять только из A-Z a-z 0-9 _")
        elif len(login) < 6:
            self.show_error("Логин должен быть больше 6 символов")
        elif len(login) > 15:
            self.show_error("Логин должен быть меньше 15 символов")
        elif len(password) < 6:
            self.show_error("Пароль должен быть больше 6 символов")
        elif len(password) > 15:
           self.show_error("Пароль должен быть меньше 15 символов")
        elif password != repeat_password:
            self.show_error("Пароли не совпадают")
        elif self.cursor.execute(f"SELECT id FROM users WHERE login = '{login}'").fetchone() is not None:
            self.show_error("Пользователь с таким логином уже существует")
        else:
            self.error_line.hide()
            
            hashed_password = hashlib.sha512(bytes(password, "utf8")).hexdigest()
            max_id = self.cursor.execute("SELECT MAX(id) FROM users").fetchone()[0] or 0

            self.cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (max_id + 1, login, hashed_password, max_id + 1))
            self.cursor.execute("INSERT INTO groups VALUES(?, ?)", (max_id + 1, ""))

            self.connection.commit()

            return True
            
        return False

    def show_error(self, error):
        self.error_line.setGeometry(QtCore.QRect(20, 530, len(error) * 12, 50))
        self.error_line.setText(error)
        self.error_line.show()
