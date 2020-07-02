# Библиотека для работы с файлами Excel
import csv

# Библиотека для использования возможностей ОС
import os

# Путь к файлу с таблицей
PATH_TO_FILE = 'cars.csv'


# Cоздание файла с таблицей и запись данных
def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Год выпуска', 'Цена', 'Город', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['year'], item['price'], item['city'], item['link']])
            print(item['title'], item['year'], item['price'], item['city'], item['link'])


# Автозапуск файла
def start_file(path):
    os.startfile(path)
