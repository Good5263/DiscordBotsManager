import os
import sqlite3

from PyQt5 import Qt

from .widgets import AddBotWidget, RemoveBotWidget, EntranceWidget, RegistrationWidget, MainProgrammWidget, InstructionWidget

class Window(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle('Discord Bots Manager')
        self.setWindowIcon(Qt.QIcon('content\images\icon.png'))

        self.connection = sqlite3.connect('content\data.sqlite')
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

        self.active_window.start_bot.clicked.connect(self.mp_start_bot)
        self.active_window.add_bot_button.clicked.connect(self.setAddBotWidget)
        self.active_window.remove_bot_button.clicked.connect(self.setRemoveBotWidget)
        self.active_window.help_button.clicked.connect(self.setInstructionWidget)
        self.active_window.unlogin_button.clicked.connect(self.setEntranceWidget)

    def mp_start_bot(self):
        pass
    
    def setInstructionWidget(self):
        self.active_window = InstructionWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.exit.clicked.connect(self.setMainProgrammWidget)

    def setAddBotWidget(self):
        self.active_window = AddBotWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.select_path_button.clicked.connect(self.active_window.select_path)
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
                id_bot, name_bot, path, token = bot
                self.active_window.all_bots_list.addItem(name_bot + '::' + path + '::' + token)
            except:
                pass

        self.active_window.remove_bot_button.clicked.connect(self.rbw_remove_bot)
        self.active_window.cancel_button.clicked.connect(self.setMainProgrammWidget)

    def rbw_remove_bot(self):
        name_bot, path, token = self.active_window.remove_bot()

        id_remove_bot = self.cursor.execute(f"SELECT ID FROM bots WHERE name_bot = '{name_bot}'").fetchone()[0]
        self.cursor.execute(f"DELETE FROM bots WHERE ID = {id_remove_bot}")
        self.connection.commit()

        self.bots = ';'.join([bot for bot in self.bots if bot != str(id_remove_bot)])
        self.cursor.execute(f"UPDATE groups SET bots = '{self.bots}' WHERE group_id = {self.group}")
        self.connection.commit()

        self.setMainProgrammWidget()