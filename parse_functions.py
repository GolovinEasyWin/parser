# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

#Библиотека для работы с HTTP-запросами
import requests

#Библиотека для трансформации DOM-дерева в Python-объект
from bs4 import BeautifulSoup

import re

# Словарь для заголовков (имитация работы браузера = антибот)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'
}

# Код успешного запроса
HTTP_OK_STATUS = 200

# Максимальное количество страниц с объявлениями
MAX_PAGES = 1000

# Максимальное количество объявлений на одной странице
MAX_CARS_ON_PAGE = 20


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

    print('cars = ', cars_count)

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
    #print(items)

    # Словарь для автомобилей
    cars = []

    # Заполняем словарь автомобилей
    for item in items:
        cars.append({
            'title': (item.find('div', class_='eozdvfu0').get_text())[:-6],
            'year': (item.find('div', class_='eozdvfu0').get_text())[-4:],
            'price':  (item.find('span', class_='css-11cjsbc').get_text())[0:-2],
            'city': item.find('span', class_='css-s9m8ro').get_text(),
            'link': item.get('href'),
        })

    return cars


def parse(url):
    # Получаем html-код
    html = get_html(url)

    # Проверка статус-кода запроса
    if html.status_code == HTTP_OK_STATUS:
        cars = []

        # Считаем количество страниц для данных аргументов
        pages_count = get_pages_count(html.text)
        print(pages_count)

        for page in range(1, pages_count + 1):
            print(f'--- Выполняется парсинг {page} страницы из {pages_count} ---')
            html = get_html(url, params={'page': page})
            cars.extend(get_content(html.text))
            #cars = get_content(html.text)
        print(cars)
        print(f'Получено {len(cars)} автомобилей!')
    else:
        print('error')
