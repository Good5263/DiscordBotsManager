import sys
from PyQt5 import Qt

from content import database
from content.window import Window


app = Qt.QApplication([])
window = Window()
window.show()
app.exec_()
