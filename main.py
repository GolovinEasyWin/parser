# Библиотека PyQT5 позволяет разрабатывать GUI
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt

from bs4 import BeautifulSoup

# Импортируем файлы с функциями и настройками для парсинга
import src.parse_functions as pf
import src.settings as st
import src.write_data as wd

# Выбор на исполнение ui-файла
Form, _ = uic.loadUiType("drom_parser.ui")


# Создание, запись в Excel-файл с последующим открытием
def start_csv(path):
    wd.start_file(path)


# Класс для работы с графическим интерфейсом пользователя (GUI)
class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('База объявлений auto.drom.ru')
        self.UI_init()

    def UI_init(self):
        # Активность при нажатии кнопки "Найти"
        self.searchButton.clicked.connect(self.searchButon_pressed)

    # Проверка checkBox "Автоматически открыть файл"
    def checkBox_condition(self, path):
        if self.checkBox.isChecked():
            start_csv(path)

    # Старт парсинга
    def searchButon_pressed(self):
        filter_car = self.filter_car()
        filter_year = self.filter_year()

        # изменить границы поиска
        url = st.create_url(filter_car, filter_year)
        cars = pf.parse(url)
        #print(cars)
        wd.save_file(cars, wd.PATH_TO_FILE)
        self.checkBox_condition(wd.PATH_TO_FILE)

    # Обработка MultiBox для выбора марки
    def filter_car(self):
        # Получение значения ComboBox для автомобиля
        car = self.comboBoxAuto.currentText()
        filter_data = car.lower()
        print(filter_data)
        return filter_data

    # Формирование comboBox для выбора модели
    # def create_comboBoxModel(self, html):
    #    soup = BeautifulSoup(html, 'html.parser')
    #    # Получаем коллекцию элементов с выбранным тегом и классом
    #    items = soup.find_all('div', class_='e1x0dvi12')
    #    models = []
    #    for item in items:
    #        models.append(item.find('div', class_='e1x0dvi12').get_text())
    #
    #    for model in models:
    #        self.comboBoxModel.addItem(model)

    # Обработка MultiBox для выбора модели
    # def filter_model(self):
    #    # Получение значения ComboBox для модели
    #    st.model = self.comboBoxModel.currentText()
    #    filter_data = st.model.lower()
    #    print(filter_data)
    #    return filter_data

    # Обработка MultiBox для ограничения года выпуска
    def filter_year(self):
        filter_year = ''
        st.year_from = self.comboBoxYear_1.currentText()
        st.year_to = self.comboBoxYear_2.currentText()

        if st.year_from != 'Любой' and st.year_to != 'Любой':
            # Если границы годов выпуска неправильные
            if st.year_from > st.year_to:
                tmp = st.year_to
                st.year_to = st.year_from
                st.year_from = tmp
            # Если указан один и тот же год выпуска
            elif st.year_from == st.year_to:
                filter_year = filter_year + '/year-' + st.year_from + '/all'
                return filter_year

        if st.year_from != 'Любой' and st.year_to != 'Любой':
            filter_year = filter_year + '/all/?minyear=' + st.year_from + '&maxyear=' + st.year_to
        elif st.year_from != 'Любой' and st.year_to == 'Любой':
            filter_year = filter_year + '/all/?minyear=' + st.year_from
        elif st.year_from == 'Любой' and st.year_to != 'Любой':
            filter_year = filter_year + '/all/?maxyear=' + st.year_to

        print(f'from {st.year_from}')
        print(f'to {st.year_to}')
        print(filter_year)
        return filter_year

    # Обработка MultiBox для ограничения цены
    def filter_price(self):
        pass


if __name__ == '__main__':
    import sys

    # Создаем приложение
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
