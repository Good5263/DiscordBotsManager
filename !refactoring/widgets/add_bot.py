from PyQt5.QtWidgets import QWidget

from ui.converted import AddBotInterface


class AddBotWidget(QWidget, AddBotInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
