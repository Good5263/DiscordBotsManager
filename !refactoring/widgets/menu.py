from PyQt5.QtWidgets import QWidget

from ui.converted import MenuInterface


class MenuWidget(QWidget, MenuInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
