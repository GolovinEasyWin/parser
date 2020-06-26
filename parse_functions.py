# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

#Библиотека для работы с HTTP-запросами
import requests

import re

#Библиотека для трансформации DOM-дерева в Python-объект
from bs4 import BeautifulSoup

# Словарь для заголовков (имитация работы браузера = антибот)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'
}

# Код успешного запроса
HTTP_OK_STATUS = 200


# Выполнение GET-запросов
def get_html(url, page_number=None):
    req = requests.get(url, headers=HEADERS, params=page_number)
    return req


def get_content(html):
    # Создание объектов Python из элементов DOM-дерева
    soup = BeautifulSoup(html, 'html.parser')
    # Получаем коллекцию элементов с выбранным тегом и классом
    items = soup.find_all('a', class_='erw2ohd2')
    #print(items)

    # Словарь для автомобилей
    cars = []
    for item in items:
        cars.append({
            'title': (item.find('div', class_='eozdvfu0').get_text())[:-6],
            'year': (item.find('div', class_='eozdvfu0').get_text())[-4:],
            'price':  (item.find('span', class_='css-11cjsbc').get_text())[0:-2],
            'link': item.get('href'),
        })

    print(cars)


def parse(url):
    # Получаем html-код
    html = get_html(url)
    # Проверка статус-кода запроса
    if html.status_code == HTTP_OK_STATUS:
        get_content(html.text)
        #print(html.text)
    else:
        print('error')
