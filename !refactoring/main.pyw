from PyQt5 import Qt

from window import MainWindow
from database import create_database


create_database("data\database.sqlite")

app = Qt.QApplication([])
window = MainWindow()
window.show()
app.exec_()
