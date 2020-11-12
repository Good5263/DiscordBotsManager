import os
import time
import sqlite3
import threading
from contextlib import redirect_stdout

from PyQt5 import Qt, QtCore

from .bot.Bot import Bot
from .widgets import (
    AddBotWidget, RemoveBotWidget, EntranceWidget,
    RegistrationWidget, MainProgrammWidget, InstructionWidget,
    ManagementBotWidget, StartBotWidget
)


def try_except(func):
    def new_func(self):
        try:
            func(self)
        except Exception as e:
            print(e)
    return new_func


class Window(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle('Discord Bots Manager')
        self.setWindowIcon(Qt.QIcon('content\images\icon.png'))

        self.connection = sqlite3.connect('content\data_files\data.sqlite')
        self.cursor = self.connection.cursor()

        self.setEntranceWidget()
    
    def setEntranceWidget(self):
        self.active_window = EntranceWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.entrance_button.clicked.connect(self.ew_validation_account)
        self.active_window.i_dont_have_account.clicked.connect(self.setRegistrationWidget)
    
    def ew_validation_account(self):
        res = self.active_window.validation_account()

        if res:
            self.active_user = res
            self.setMainProgrammWidget()

    def setRegistrationWidget(self):
        self.active_window = RegistrationWidget()
        self.setCentralWidget(self.active_window)
        
        self.active_window.registation_button.clicked.connect(self.rw_validation_account)
        self.active_window.i_have_account.clicked.connect(self.setEntranceWidget)
    
    def rw_validation_account(self):
        valid = self.active_window.validation_account()

        if valid:
            self.active_user = valid
            self.setMainProgrammWidget()
    
    def setMainProgrammWidget(self):
        self.active_window = MainProgrammWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.start_bot.clicked.connect(self.setStartBotWidget)
        self.active_window.add_bot_button.clicked.connect(self.setAddBotWidget)
        self.active_window.remove_bot_button.clicked.connect(self.setRemoveBotWidget)
        self.active_window.help_button.clicked.connect(self.setInstructionWidget)
        self.active_window.unlogin_button.clicked.connect(self.setEntranceWidget)

    def setInstructionWidget(self):
        self.active_window = InstructionWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.exit.clicked.connect(self.setMainProgrammWidget)

    def setAddBotWidget(self):
        self.active_window = AddBotWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.add_bot_button.clicked.connect(self.abw_add_bot)
        self.active_window.cancel_button.clicked.connect(self.setMainProgrammWidget)

    def abw_add_bot(self):
        res = self.active_window.add_bot()
        if not res:
            return
        
        num = str(res)
        group = self.cursor.execute(f"SELECT group_bots FROM users WHERE login = '{self.active_user}'").fetchone()[0]
        bots = self.cursor.execute(f"SELECT bots FROM groups WHERE group_id = {group}").fetchone()[0]

        new_bots = bots + ';' + num
        if new_bots.startswith('0;'):
            new_bots = new_bots[2:]
        elif new_bots.startswith(';'):
            new_bots = new_bots[1:]

        self.cursor.execute(f"UPDATE groups SET bots = '{new_bots}' WHERE group_id = {group}")
        self.connection.commit()

        self.setMainProgrammWidget()
    
    def setRemoveBotWidget(self):
        self.active_window = RemoveBotWidget()
        self.setCentralWidget(self.active_window)

        self.group = self.cursor.execute(f"SELECT group_bots FROM users WHERE login = '{self.active_user}'").fetchone()[0]
        bots = self.cursor.execute(f"SELECT bots FROM groups WHERE group_id = {self.group}").fetchone()[0]
        self.bots = bots.split(';')

        for bot in self.bots:
            try:
                bot = self.cursor.execute(f"SELECT * FROM bots WHERE ID = {bot}").fetchone()
                id_bot, name_bot, token = bot
                self.active_window.all_bots_list.addItem(name_bot + '::' + token)
            except:
                pass

        self.active_window.remove_bot_button.clicked.connect(self.rbw_remove_bot)
        self.active_window.cancel_button.clicked.connect(self.setMainProgrammWidget)

    @try_except
    def rbw_remove_bot(self):
        name_bot, token = self.active_window.remove_bot()

        id_remove_bot = self.cursor.execute(f"SELECT ID FROM bots WHERE name_bot = '{name_bot}'").fetchone()[0]
        self.cursor.execute(f"DELETE FROM bots WHERE ID = {id_remove_bot}")
        self.connection.commit()

        self.bots = ';'.join([bot for bot in self.bots if bot != str(id_remove_bot)])
        self.cursor.execute(f"UPDATE groups SET bots = '{self.bots}' WHERE group_id = {self.group}")
        self.connection.commit()

        self.setMainProgrammWidget()
    
    def setStartBotWidget(self):
        self.active_window = StartBotWidget()
        self.setCentralWidget(self.active_window)

        self.group = self.cursor.execute(f"SELECT group_bots FROM users WHERE login = '{self.active_user}'").fetchone()[0]
        bots = self.cursor.execute(f"SELECT bots FROM groups WHERE group_id = {self.group}").fetchone()[0]
        self.bots = bots.split(';')

        for bot in self.bots:
            try:
                bot = self.cursor.execute(f"SELECT * FROM bots WHERE ID = {bot}").fetchone()
                id_bot, name_bot, token = bot
                self.active_window.bots.addItem(name_bot + '::' + token)
            except:
                pass
        
        self.active_window.start_bot_button.clicked.connect(self.setManagementBotWidget)
        self.active_window.exit_button.clicked.connect(self.setMainProgrammWidget)
    
    def setManagementBotWidget(self):
        name, token = self.active_window.bots.currentText().split('::')
        
        self.active_window = ManagementBotWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.top_name_line.setText(name)
        self.active_window.middle_token_line.setText(token)

        self.active_bot = Bot(token)
        bot_thread = threading.Thread(target=self.mbw_start_bot)
        bot_thread.start()
        time.sleep(2)

        self.mbw_update_nickname()
        self.mbw_update_count_guilds()

        for cog in os.listdir('content/bot/cogs'):
            if cog.endswith('.py'):
                self.active_window.on_cogs.addItem(cog[:-3])

        self.active_window.update_status.clicked.connect(self.mbw_update_status)
        self.active_window.update_user_status.clicked.connect(self.mbw_update_activity)
        self.active_window.update_count_guilds.clicked.connect(self.mbw_update_count_guilds)
        self.active_window.nick_update_button.clicked.connect(self.mbw_update_nickname)

        self.active_window.connect.clicked.connect(self.mbw_load_cog)
        self.active_window.disconnect.clicked.connect(self.mbw_unload_cog)

        self.active_window.exit_button.clicked.connect(self.setMainProgrammWidget)
    
    def mbw_start_bot(self):
        with redirect_stdout(None):
            self.active_bot.on_bot()
    
    @try_except
    def mbw_update_activity(self):
        item = self.active_window.user_status_line.text()
        self.active_bot.activity_update(item)
    
    @try_except
    def mbw_update_status(self):
        item = self.active_window.select_status.currentText()
        self.active_bot.status_update(item)
    
    @try_except
    def mbw_update_count_guilds(self):
        item = str(len(self.active_bot.client.guilds))
        self.active_window.count_guilds_line.setText(item)
    
    @try_except
    def mbw_update_nickname(self):
        self.active_window.nick_line.setText(str(self.active_bot.client.user))
    
    @try_except
    def mbw_load_cog(self):
        cog = self.active_window.off_cogs.currentText()
        cog_index = self.active_window.off_cogs.currentIndex()

        if cog == '':
            return

        self.active_window.off_cogs.removeItem(cog_index)
        self.active_window.on_cogs.addItem(cog)
        
        self.active_bot.load_cog(cog)

    @try_except
    def mbw_unload_cog(self):
        cog = self.active_window.on_cogs.currentText()
        cog_index = self.active_window.on_cogs.currentIndex()

        if cog == '':
            return

        self.active_window.on_cogs.removeItem(cog_index)
        self.active_window.off_cogs.addItem(cog)
        
        self.active_bot.unload_cog(cog)
