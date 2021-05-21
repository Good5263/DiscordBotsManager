import sqlite3
from PyQt5.QtWidgets import QWidget

from ui.converted import StartBotInterface


class StartBotWidget(QWidget, StartBotInterface):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = user_login
