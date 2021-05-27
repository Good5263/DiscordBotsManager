import sqlite3
import hashlib

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from ui.converted import SignInInterface


class SignInWidget(QWidget, SignInInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.error_line.hide()

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()
    
    def data_validation(self):
        self.error_line.hide()

        login = self.login.text()
        password = self.password.text()

        if login.isspace() or password.isspace() or not login or not password:
            self.show_error("Поля логина и пароля должны быть заполнены")
            return (False, None)
        
        hashed_password = self.cursor.execute(f"SELECT hashed_password FROM users WHERE login = '{login}'").fetchone()[0]

        if hashed_password == hashlib.sha512(bytes(password, "utf8")).hexdigest():
            return (True, login)
        
        self.show_error("Неправильный логин или пароль")
        return (False, None)
    
    def show_error(self, error):
        self.error_line.setGeometry(QtCore.QRect(20, 530, len(error) * 12, 50))
        self.error_line.setText(error)
        self.error_line.show()
