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

        self.show_all_bots()
    
    def show_all_bots(self):
        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0]
        bot_ids_list = bot_ids_list.split(";") if bot_ids_list else []

        for bot_id in map(int, bot_ids_list):
            name, token = self.cursor.execute(f"SELECT name, token FROM bots WHERE id = {bot_id}").fetchone()
            self.list_bots.addItem(str(bot_id) + "::" + name + "::" + token)
    
    def get_selected_bot(self):
        _, name, token = self.list_bots.currentText().split("::")
        return name, token
