# ©LG, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

# Библиотека для использования командной строки
import sys

# Инициализация переменных под аргументы КС
car = 0
city = 0
year_from = 0
year_to = 0
price_from = 0
price_to = 0

# Список с действующими марками автомобилей
LIST_CARS = [
    'acura', 'audi', 'bmw', 'chery', 'chevrolet', 'citroen',
    'daewoo', 'fiat', 'ford', 'honda', 'hyundai', 'kia',
    'mazda', 'lexus', 'mercedes-benz', 'mitsubishi',
    'nissan', 'opel', 'peugeot', 'renault', 'skoda',
    'subaru', 'suzuki', 'toyota', 'volkswagen', 'volvo'
]


# Проверка введенных пользователем аргументов
def check_arguments(filter_car):
    if filter_car in LIST_CARS:
        return True


def create_region_number(region):
    region_number = 0
    if region == 'Санкт-Петербург':
        region_number = 78
    elif region == 'Москва':
        region_number = 77
    elif region == 'Новосибирская область':
        region_number = 54
    elif region == 'Свердловская область':
        region_number = 66
    elif region == 'Республика Татарстан':
        region_number = 16
    elif region == 'Волгоградская область':
        region_number = 34
    elif region == 'Пермский край':
        region_number = 59
    elif region == 'Ростовская область':
        region_number = 61
    return region_number


# Формирование URL страницы для передачи в parse_functions.py
def create_url(filter_region, filter_car, filter_year, filter_price):
    # Базовый адрес сайта
    default_url = 'https://auto.drom.ru/'

    if check_arguments(filter_car):

        if str(filter_year).isdigit():
            adress = default_url + 'region' + str(create_region_number(filter_region)) + '/' + str(filter_car) + '/year-' + filter_year + '/all/' + filter_price
        else:
            # Возвращаем новый адрес с учетом аргументов
            adress = default_url + 'region' + str(create_region_number(filter_region)) + '/' + str(filter_car) + '/all/' + filter_price + filter_year
        print(f'adress = {adress}')
        return adress
    # Завершение работы программы при неверном вводе аргументов
    else:
        print('Ошибка')
        sys.exit()
