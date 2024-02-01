import sys
import pprint
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:


def get_spn(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coord1 = list(map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split()))
    coord2 = list(map(float, toponym['boundedBy']['Envelope']['upperCorner'].split()))
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    spn = f'{abs(coord1[0] - coord2[0]) / 2.0},{abs(coord1[1] - coord2[1]) / 2.0}'
    ll = ",".join([toponym_longitude, toponym_lattitude])
    return ll, spn


def get_map(place):
    ll, spn = get_spn(place)
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        'pt': "{0},pm2dgl".format(ll)
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()




if __name__ == "__main__":
    toponym_to_find = " ".join(sys.argv[1:])
    if not toponym_to_find:
        toponym_to_find = input('Введите объект для поиска: ')
    get_map(toponym_to_find)
