# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

# Библиотека для использования командной строки
import sys

# Урезаем массив с аргументами КС
arguments = sys.argv[1:]

# Инициализация переменных под аргументы КС
arg1 = str(arguments[0])
#arg2 = arguments[1]

# Список с действующими марками автомобилей
LIST_CARS = [
    'audi', 'bmw', 'chevrolet', 'daewoo',
    'ford', 'honda', 'hyundai', 'kia',
    'mazda', 'mercedes-benz', 'mitsubishi',
    'nissan', 'opel', 'renault', 'skoda',
    'subaru', 'toyota', 'volkswagen', 'lada'
]


# Проверка введенных пользователем аргументов
def check_arguments(car):
    if car in LIST_CARS:
        return True


# Формирование URL страницы для передачи в parse_functions.py
def create_url(car):
    # Базовый адрес сайта
    default_url = 'https://auto.drom.ru/'
    if check_arguments(car):
        # Возвращаем новый адрес с учетом аргументов
        return default_url + car
    # Завершение работы программы при неправильном вводе аргументов
    else:
        print('Ошибка ввода аргументов')
        sys.exit()
