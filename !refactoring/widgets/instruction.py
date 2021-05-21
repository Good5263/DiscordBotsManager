from PyQt5.QtWidgets import QWidget

from ui.converted import InstructionInterface


class InstructionWidget(QWidget, InstructionInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
