import sqlite3

from PyQt5 import QtWidgets
from .ui_classes import RemoveBot

class RemoveBotWidget(RemoveBot):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('programm\content\data_files\data.sqlite')
        self.cursor = self.connection.cursor()

        self.all_bots_list.itemSelectionChanged.connect(self.select_bot)
    
    def select_bot(self):
        item = self.all_bots_list.currentItem() 
        self.name_bot_line.setText(item.text())
    
    def remove_bot(self):
        return self.name_bot_line.text().split('::')
