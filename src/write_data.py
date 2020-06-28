# Библиотека для работы с файлами Excel
import csv


import os

# Путь к файлу с таблицей
PATH_TO_FILE = 'cars.csv'


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Год выпуска', 'Цена', 'Город', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['year'], item['price'], item['city'], item['link']])


def start_file(path):
    os.startfile(path)
