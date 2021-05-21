from PyQt5.QtWidgets import QWidget

from ui.converted import StartBotInterface


class StartBotWidget(QWidget, StartBotInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
