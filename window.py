import sqlite3

from PyQt5 import Qt

from widgets import (
    SignUpWidget, SignInWidget, MenuWidget,
    AddBotWidget, RemoveBotWidget, StartBotWidget,
    InstructionWidget, BotManagementWidget
)


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle("Discord Bots Manager")
        self.setWindowIcon(Qt.QIcon("images\icon.png"))

        self.connection = sqlite3.connect("data\database.sqlite")
        self.cursor = self.connection.cursor()

        self.user_login = None

        self.set_sign_in_window()
    
    def set_sign_in_window(self):
        self.active_window = SignInWidget()
        self.setCentralWidget(self.active_window)
        
        self.active_window.sign_in_button.clicked.connect(self.sign_in_to_account)
        self.active_window.i_dont_have_accont.clicked.connect(self.set_sign_up_window)

    def set_sign_up_window(self):
        self.active_window = SignUpWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.sign_up_button.clicked.connect(self.registation_account)
        self.active_window.i_have_accont.clicked.connect(self.set_sign_in_window)
    
    def set_menu_window(self):
        self.active_window = MenuWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.start_bot_button.clicked.connect(self.set_start_bot_window)
        self.active_window.add_bot_button.clicked.connect(self.set_add_bot_window)
        self.active_window.remove_bot_button.clicked.connect(self.set_remove_bot_window)
        self.active_window.show_instruction_button.clicked.connect(self.set_show_instruction_window)
        self.active_window.logout_button.clicked.connect(self.set_sign_in_window)
    
    def set_management_bot_widget(self, name, token):
        self.active_window = BotManagementWidget(name, token)
        self.setCentralWidget(self.active_window)

        self.active_window.exit_to_menu_button.clicked.connect(self.set_menu_window)

    def set_start_bot_window(self):
        self.active_window = StartBotWidget(self.user_login)
        self.setCentralWidget(self.active_window)

        self.active_window.exit_to_menu_button.clicked.connect(self.set_menu_window)
        self.active_window.start_bot_button.clicked.connect(self.start_bot)

    def set_add_bot_window(self):
        self.active_window = AddBotWidget(self.user_login)
        self.setCentralWidget(self.active_window)

        self.active_window.exit_to_menu_button.clicked.connect(self.set_menu_window)

    def set_remove_bot_window(self):
        self.active_window = RemoveBotWidget(self.user_login)
        self.setCentralWidget(self.active_window)

        self.active_window.exit_to_menu_button.clicked.connect(self.set_menu_window)

    def set_show_instruction_window(self):
        self.active_window = InstructionWidget()
        self.setCentralWidget(self.active_window)

        self.active_window.exit_to_menu_button.clicked.connect(self.set_menu_window)
    
    def registation_account(self):
        successfuly = self.active_window.validation_account()

        if successfuly:
            self.set_sign_in_window()

    def sign_in_to_account(self):
        successfuly, login = self.active_window.data_validation()

        if successfuly:
            self.user_login = login
            self.set_menu_window()
    
    def start_bot(self):
        name, token = self.active_window.get_selected_bot()
        self.set_management_bot_widget(name, token)
