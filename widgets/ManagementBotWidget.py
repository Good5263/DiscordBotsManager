from PyQt5 import QtWidgets
from .ui_classes import ManagementBot


class ManagementBotWidget(ManagementBot):
    def __init__(self):
        super().__init__()

        self.hide_count = 1
        self.hide_name_count = 1
        self.hide_token_count = 1
        self.hide_cogs_count = 1

        self.top_show_or_hide.clicked.connect(self.top_soh_toggle)
        self.middle_show_or_hide.clicked.connect(self.middle_soh_toggle)
        self.show_or_hide.clicked.connect(self.hide_all)

    def hide_all(self):
        self.hide_count = (self.hide_count + 1) % 2

        elements = [
            self.top_name_label, self.top_name_line, self.top_show_or_hide,
            self.middle_token_label, self.middle_token_line, self.middle_show_or_hide,
            self.cogs_label, self.connect, self.disconnect, self.on_cogs, self.off_cogs
        ]

        if self.hide_count:
            self.show_or_hide.setText('Скрыть информацию')
            for el in elements:
                el.show()
        else:
            self.show_or_hide.setText('Показать информацию')
            for el in elements:
                el.hide()
    
    def top_soh_toggle(self):
        self.hide_name_count = (self.hide_name_count + 1) % 2

        if self.hide_name_count:
            self.top_show_or_hide.setText('+')
            self.top_name_line.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.top_show_or_hide.setText('-')
            self.top_name_line.setEchoMode(QtWidgets.QLineEdit.Normal)

    def middle_soh_toggle(self):
        self.hide_token_count = (self.hide_token_count + 1) % 2

        if self.hide_token_count:
            self.middle_show_or_hide.setText('+')
            self.middle_token_line.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.middle_show_or_hide.setText('-')
            self.middle_token_line.setEchoMode(QtWidgets.QLineEdit.Normal)
