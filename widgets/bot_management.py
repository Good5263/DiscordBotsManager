import threading

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from ui.converted import BotManagementInterface
from bot.bot import Bot


class BotManagementWidget(QWidget, BotManagementInterface):
    def __init__(self, name, token):
        super().__init__()
        self.setupUi(self)

        self.hide_information = 0
        self.hide_name = 1
        self.hide_token = 1

        self.name = name
        self.token = token

        self.bot = Bot(token)
        self.bot_started = False
        
        self.run_bot()

        self.nickname_bot_update_button.clicked.connect(self.show_nickname_bot)
        self.servers_count_update_button.clicked.connect(self.show_servers_count)
        self.users_count_update_button.clicked.connect(self.show_users_count)
        self.activity_status_bot_update_button.clicked.connect(self.change_activity_status)
        self.status_bot_update_button.clicked.connect(self.change_status)
        self.unload_command_button.clicked.connect(self.unload_cog)
        self.load_command_button.clicked.connect(self.load_cog)
        self.show_or_hide_name_bot_button.clicked.connect(self.show_or_hide_name_toggle)
        self.show_or_hide_token_bot_button.clicked.connect(self.show_or_hide_token_toggle)
        self.show_or_hide_information_button.clicked.connect(self.show_or_hide_information_toggle)
    
    def run_bot(self):
        thread = threading.Thread(target=self.bot.run_bot, daemon=True)
        thread.start()
        
        self.bot_started = True
        self.name_bot.setText(self.name)
        self.token_bot.setText(self.token)

        self.show_nickname_bot()
        self.show_servers_count()        
        self.show_users_count()
        self.show_all_cogs()
    
    def show_or_hide_information_toggle(self):
        self.hide_information = 1 - self.hide_information

        components = [
            self.name_bot_label, self.name_bot, self.show_or_hide_name_bot_button,
            self.token_bot_label, self.token_bot, self.show_or_hide_token_bot_button,
            self.commands_label, self.unload_command_button, self.unloaded_commands_list,
            self.load_command_button, self.loaded_commands_list
        ]

        if self.hide_information:
            self.show_or_hide_information_button.setText("Показать информацию")
            for component in components:
                component.hide()
        else:
            self.show_or_hide_information_button.setText("Скрыть информацию")
            for component in components:
                component.show()

    def show_or_hide_name_toggle(self):
        self.hide_name = 1 - self.hide_name

        if self.hide_name:
            self.show_or_hide_name_bot_button.setText("+")
            self.name_bot.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.show_or_hide_name_bot_button.setText("-")
            self.name_bot.setEchoMode(QtWidgets.QLineEdit.Normal)
    
    def show_or_hide_token_toggle(self):
        self.hide_token = 1 - self.hide_token

        if self.hide_token:
            self.show_or_hide_token_bot_button.setText("+")
            self.token_bot.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.show_or_hide_token_bot_button.setText("-")
            self.token_bot.setEchoMode(QtWidgets.QLineEdit.Normal)
    
    def show_all_cogs(self):
        for cog in self.bot.get_loaded_cogs():
            self.loaded_commands_list.addItem(cog)
    
    def show_nickname_bot(self):
        if self.bot.runned:
            self.nickname_bot.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
            self.nickname_bot.setText(str(self.bot.client.user))   
        else:
            self.nickname_bot.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";color: rgb(255, 0, 0)")
            self.nickname_bot.setText("Bot not started")
    
    def show_servers_count(self):
        self.servers_count.setText(str(self.bot.get_guilds_count()))
    
    def show_users_count(self):
        self.users_count.setText(str(self.bot.get_members_count()))
    
    def change_activity_status(self):
        if self.bot.runned:
            self.bot.activity_status_update(self.activity_status_bot_list.currentText())

    def change_status(self):
        if self.bot.runned:
            self.status_bot.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
            self.bot.status_update(self.status_bot.text())
        else:
            self.status_bot.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";color: rgb(255, 0, 0)")
            self.status_bot.setText("Bot not started")
    
    def load_cog(self):
        cog = self.unloaded_commands_list.currentText()
        cog_index = self.unloaded_commands_list.currentIndex()

        if cog == '':
            return

        self.unloaded_commands_list.removeItem(cog_index)
        self.loaded_commands_list.addItem(cog)
        
        self.bot.load_cog(cog)

    def unload_cog(self):
        cog = self.loaded_commands_list.currentText()
        cog_index = self.loaded_commands_list.currentIndex()

        if cog == '':
            return

        self.loaded_commands_list.removeItem(cog_index)
        self.unloaded_commands_list.addItem(cog)
        
        self.bot.unload_cog(cog)
