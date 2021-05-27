import sqlite3
from PyQt5.QtWidgets import QWidget

from ui.converted import AddBotInterface


class AddBotWidget(QWidget, AddBotInterface):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)

        self.error_line.hide()

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = user_login

        self.show_all_bots()

        self.add_bot_button.clicked.connect(self.add_bot)
    
    def show_all_bots(self):
        self.list_bots.clear()

        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0]
        bot_ids_list = bot_ids_list.split(";") if bot_ids_list else []

        for bot_id in map(int, bot_ids_list):
            name, token = self.cursor.execute(f"SELECT name, token FROM bots WHERE id = {bot_id}").fetchone()
            self.list_bots.addItem(str(bot_id) + "::" + name + "::" + token)
    
    def add_bot(self):
        name = self.bot_name.text()
        token = self.bot_token.text()

        if name.isspace() or token.isspace() or not token or not name:
            self.show_error("Поля токена и имени бота должны быть заполнены")
            return
        
        if ":" in token or ":" in name:
            self.show_error("Токен и/или название не должны содержать \":\"")
            return

        max_id = self.cursor.execute("SELECT MAX(id) FROM bots").fetchone()[0] or 0
        self.cursor.execute("INSERT INTO bots VALUES(?, ?, ?)", (max_id + 1, name, token))

        bot_group_id = self.cursor.execute(f"SELECT bot_group_id FROM users WHERE login = '{self.user_login}'").fetchone()[0]
        bot_ids_list = self.cursor.execute(f"SELECT bot_ids FROM groups WHERE id = {bot_group_id}").fetchone()[0]
        bot_ids_list = bot_ids_list.split(";") if bot_ids_list else []
        bot_ids_list.append(str(max_id + 1))

        self.cursor.execute(f"UPDATE groups SET bot_ids = '{';'.join(bot_ids_list)}' WHERE id = {bot_group_id}")

        self.connection.commit()

        self.show_all_bots()
        self.bot_name.setText("")
        self.bot_token.setText("")
    
    def show_error(self, error):
        self.error_line.setText(error)
        self.error_line.show()
