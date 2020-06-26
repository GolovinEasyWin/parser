# Библиотека для использования командной строки
import sys

# Урезаем массив с аргументами КС
arguments = sys.argv[1:]

# Инициализация переменных под аргументы КС
arg1 = arguments[0]
arg2 = arguments[1]

# Список с действующими марками автомобилей
LIST_CARS = [
    'acura', 'alfa_romeo', 'alphina',
    'asia', 'aston_martin', 'audi',
    'bentley', 'bmw', 'brilliance',
    'buick', 'byd', 'cadilac'
]


# Проверка введенных пользователем аргументов
def check_arguments(car):
    if car in LIST_CARS:
        return True


# Формирование URL страницы для передачи в parser.py
def create_url(car):
    # Базовый адрес сайта
    default_url = 'https://www.drom.ru/'
    if check_arguments(car):
        # Возвращаем новый адрес с учетом аргументов
        return default_url + car
    else:
        print('Ошибка ввода аргументов')
        return -1


#URL = create_url(arg1)
