from PyQt5.QtWidgets import QWidget

from ui.converted import BotManagementInterface


class BotManagementWidget(QWidget, BotManagementInterface):
    def __init__(self, name, token):
        super().__init__()
        self.setupUi(self)
