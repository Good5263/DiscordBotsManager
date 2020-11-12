from contextlib import redirect_stdout

from PyQt5 import Qt

from content import database
from content.window import Window


with redirect_stdout(None):
    app = Qt.QApplication([])
    window = Window()
    window.show()
    app.exec_()
