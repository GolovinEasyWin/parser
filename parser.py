# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

# Импортируем все объекты и методы из файла settings.py
import settings

#Библиотека для работы с HTTP-запросами
import requests

#Библиотека для трансформации DOM-дерева в Python-объект
from bs4 import BeautifulSoup

# Словарь для заголовков (имитация работы браузера = антибот)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'
}

URL = 'https://www.drom.ru'

# Код успешного запроса
HTTP_OK = 200


# Выполнение GET-запросов
def get_html(url, page_number=None):
    req = requests.get(url, headers=HEADERS, params=page_number)
    return req


def get_content(html):
    # Создание объектов Python из элементов DOM-дерева
    soup = BeautifulSoup(html, 'html.parser')
    # Получаем коллекцию элементов с выбранным тегом и классом
    items = soup.find_all('a', '')


def parse():
    html = get_html(URL)
    if html.status_code == HTTP_OK:
        get_content(html.text)
    else:
        print('error')
