# Библиотека PyQT5 позволяет разрабатывать GUI
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# Выбор на исполнение ui-файла
Form, Window = uic.loadUiType("drom_parser.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
