# Библиотека PyQT5 позволяет разрабатывать GUI
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt

# Импортируем файлы с функциями и настройками для парсинга
import src.parse_functions as pf
import src.settings as st
import src.write_data as wd

# Выбор на исполнение ui-файла
Form, _ = uic.loadUiType("drom_parser.ui")


# Создание, запись в Excel-файл с последующим открытием
def create_csv(cars):
    wd.save_file(cars, wd.PATH_TO_FILE)
    wd.start_file(wd.PATH_TO_FILE)


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('База объявлений auto.drom.ru')
        self.UI_init()

    def UI_init(self):
        # Активность при нажатии кнопки "Найти"
        cars = self.searchButton.clicked.connect(self.searchButon_pressed)

    # Проверка checkBox "Сгенерировать Excel-файл"
    def checkBox_condition(self, cars):
        if self.checkBox.isChecked():
            create_csv(cars)

    # Старт парсинга
    def searchButon_pressed(self):
        url = st.create_url('acura')
        cars = pf.parse(url)
        self.checkBox_condition(cars)

    # Обработка MultiBox для фильтрации поиска
    def filter(self):
        pass


if __name__ == '__main__':
    import sys

    # Создаем приложение
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
