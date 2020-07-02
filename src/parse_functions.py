# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

#Библиотека для работы с HTTP-запросами
import requests

#Библиотека для трансформации DOM-дерева в Python-объект
from bs4 import BeautifulSoup

import src.settings as st

#Библиотека для использования регулярных выражений
import re

# Словарь для заголовков (имитация работы браузера = антибот)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'
}

# Код успешного запроса
HTTP_OK_STATUS = 200

# Максимальное количество страниц с объявлениями
MAX_PAGES = 100

# Максимальное количество объявлений на одной странице
MAX_CARS_ON_PAGE = 20

# Словарь для автомобилей
cars = []


# Выполнение GET-запросов
def get_html(url, params=None):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_pages_count(html):
    # Создание объектов Python из элементов DOM-дерева
    soup = BeautifulSoup(html, 'html.parser')

    # Находим число объявлений по запросу
    cars_count = soup.find('button', class_='e75dypj1').get_text()

    cars_count = int(re.sub(r'[^0-9]', r'', cars_count))

    # Проверка на одну страницу
    if cars_count <= MAX_CARS_ON_PAGE:
        return 1

    # Выполняем целочисленное деление для нахождения количества страниц
    pages_count = cars_count // MAX_CARS_ON_PAGE + 1
    return pages_count


def get_content(html):
    # Создание объектов Python из элементов DOM-дерева
    soup = BeautifulSoup(html, 'html.parser')

    # Получаем коллекцию элементов с выбранным тегом и классом
    items = soup.find_all('a', class_='erw2ohd2')

    error_page = soup.find_all('div', type='warning')

    if not items or error_page:
        return -1

    # Заполняем словарь автомобилей
    for item in items:
        new_info = {
            'title': (item.find('div', class_='eozdvfu0').get_text())[:-6],
            'year': (item.find('div', class_='eozdvfu0').get_text())[-4:],
            'price':  (item.find('span', class_='css-11cjsbc').get_text())[0:-2],
            'city': item.find('span', class_='css-s9m8ro').get_text().replace('\u2192', '-'),
            'link': item.get('href'),
        }
        if new_info in cars:
            #print(new_info)
            return -1
        cars.append(new_info)
    return cars


def parse(url):
    print(f'url in parse = {url}')
    # Получаем html-код
    html = get_html(url)

    # Проверка статус-кода запроса
    if html.status_code == HTTP_OK_STATUS:

        pages = MAX_PAGES
        if st.year_from == 'Любой' and st.year_to == 'Любой': #and st.price_from == 'Любая' and st.price_to == 'Любая':
            pages = get_pages_count(html.text)

        result = 0
        for page in range(1, pages + 1):
            print(f'--- Выполняется парсинг {page} страницы ---')
            html = get_html(url, params={'page': page})
            result = get_content(html.text)
            if result != -1:
                cars.extend(result)
            else:
                break
        return result
    else:
        print('error')
