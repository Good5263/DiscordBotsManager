import sqlite3

from PyQt5 import Qt

from widgets import (
    SignUpWidget, SignInWidget
)


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle("Discord Bots Manager")
        self.setWindowIcon(Qt.QIcon("images\icon.png"))

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = None

        self.set_sign_in_window()
    
    def set_sign_in_window(self):
        self.active_window = SignInWidget()
        self.setCentralWidget(self.active_window)
        
        self.active_window.sign_in_button.clicked.connect(self.sign_in_to_account)
        self.active_window.i_dont_have_accont.clicked.connect(self.set_sign_up_window)

    def set_sign_up_window(self):
        self.active_window = SignUpWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.sign_up_button.clicked.connect(self.registation_account)
        self.active_window.i_have_accont.clicked.connect(self.set_sign_in_window)
    
    def registation_account(self):
        successfuly = self.active_window.validation_account()

        if successfuly:
            self.set_sign_in_window()

    def sign_in_to_account(self):
        successfuly, login = self.active_window.data_validation()

        if successfuly:
            self.user_login = login
