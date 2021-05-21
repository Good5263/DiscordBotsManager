import sqlite3
from PyQt5.QtWidgets import QWidget

from ui.converted import AddBotInterface


class AddBotWidget(QWidget, AddBotInterface):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = user_login
    
    def add_bot(self):
        name = self.bot_name.text()
        token = self.bot_token.text()

        if name.isspace() or token.isspace() or not token or not name:
            return

        max_id = self.cursor.execute("SELECT MAX(id) FROM bots").fetchone()[0] or 0
        self.cursor.execute("INSERT INTO bots VALUES(?, ?, ?)", (max_id + 1, name, token))

        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0]
        bot_ids_list = bot_ids_list.split(";") if bot_ids_list else []
        bot_ids_list.append(str(max_id + 1))

        self.cursor.execute(f"UPDATE groups SET bot_ids = '{';'.join(bot_ids_list)}' WHERE id = {bot_group_id}")

        self.connection.commit()
