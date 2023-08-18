import sys
from PySide6.QtWidgets import QApplication
from main_window import *

app=QApplication(sys.argv)
window=MainWindow(app)

window.show()

app.exec()
