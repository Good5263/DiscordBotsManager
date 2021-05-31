import sqlite3
from PyQt5.QtWidgets import QWidget

from ui.converted import RemoveBotInterface


class RemoveBotWidget(QWidget, RemoveBotInterface):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = user_login

        self.show_all_bots()

        self.list_bots.itemSelectionChanged.connect(self.select_bot)
        self.remove_bot_button.clicked.connect(self.remove_bot)
    
    def show_all_bots(self):
        self.list_bots.clear()

        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0]
        bot_ids_list = bot_ids_list.split(";") if bot_ids_list else []

        for bot_id in map(int, bot_ids_list):
            name, token = self.cursor.execute(f"SELECT name, token FROM bots WHERE id = {bot_id}").fetchone()
            self.list_bots.addItem(str(bot_id) + "::" + name + "::" + token)
    
    def select_bot(self):
        item = self.list_bots.currentItem().text()
        self.remove_bot_info.setText(item)
    
    def remove_bot(self):
        remove_bot_info = self.remove_bot_info.text()

        if remove_bot_info.isspace() or not remove_bot_info:
            return

        bot_id = int(remove_bot_info.split("::")[0])

        self.cursor.execute(f"DELETE FROM bots WHERE id = {bot_id}")

        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0].split(";")
        bot_ids_list.remove(str(bot_id))

        self.cursor.execute(f"UPDATE groups SET bot_ids = '{';'.join(bot_ids_list)}' WHERE id = {bot_group_id}")

        self.connection.commit()

        self.show_all_bots()
        self.remove_bot_info.setText("")
