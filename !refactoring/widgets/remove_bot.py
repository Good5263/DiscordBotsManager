from PyQt5.QtWidgets import QWidget

from ui.converted import RemoveBotInterface


class RemoveBotWidget(QWidget, RemoveBotInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
