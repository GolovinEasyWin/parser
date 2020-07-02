# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

# Библиотека для использования командной строки
import sys

# Инициализация переменных под аргументы КС
car = 0
year_from = 0
year_to = 0
price_from = 0
price_to = 0

# Список с действующими марками автомобилей
LIST_CARS = [
    'audi', 'bmw', 'chevrolet', 'daewoo',
    'ford', 'honda', 'hyundai', 'kia',
    'mazda', 'mercedes-benz', 'mitsubishi',
    'nissan', 'opel', 'renault', 'skoda',
    'subaru', 'toyota', 'volkswagen', 'acura'
]


# Проверка введенных пользователем аргументов
def check_arguments(filter_car):
    if filter_car in LIST_CARS:
        return True


# Формирование URL страницы для передачи в parse_functions.py
def create_url(filter_car, filter_year):
    # Базовый адрес сайта
    default_url = 'https://auto.drom.ru/'

    if check_arguments(filter_car):
        # Возвращаем новый адрес с учетом аргументов
        adress = default_url + str(filter_car) + filter_year
        print(f'adress = {adress}')
        return adress
    # Завершение работы программы при неверном вводе аргументов
    else:
        print('Ошибка ввода аргументов')
        sys.exit()
