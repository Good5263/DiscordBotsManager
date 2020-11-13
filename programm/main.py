import asyncio
from contextlib import redirect_stdout

from PyQt5 import Qt

from content import database
from content.window import Window


outlog = open("programm\content\data_files\outlog.txt", mode="w")

with redirect_stdout(outlog):
    app = Qt.QApplication([])
    window = Window()
    window.show()
    app.exec_()

    try:
        asyncio.ensure_future(window.active_bot.client.logout())
    except Exception as e:
        print(e)

outlog.close()
