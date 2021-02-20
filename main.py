import asyncio

from PyQt5 import Qt

from database import create_database
from window import Window


create_database()

app = Qt.QApplication([])
window = Window()
window.show()
app.exec_()

try:
    asyncio.ensure_future(window.active_bot.client.logout())
except Exception as e:
    print(e)
