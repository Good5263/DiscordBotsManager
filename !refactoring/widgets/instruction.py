from PyQt5.QtWidgets import QWidget

from ui.converted import InstructionInterface


class InstructionWidget(QWidget, InstructionInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        inctruction_text = open("data\instruction.txt", mode="r", encoding="utf8").read()
        self.inctruction.setPlainText(inctruction_text)
