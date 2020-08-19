import functools

import requests
from datetime import datetime
import time


def get_datetime():
    actual_time = datetime.now()
    formatted_time = actual_time.strftime("%d.%m.%Y %H:%M:%S")
    return f'Data i godzina: {formatted_time}'


def get_res_time(res):
    @functools.wraps(res)
    def wrapper(*args, **kwargs):
        milisec = int(res().elapsed.microseconds * 0.001)
        print(f'Czas wykonania zapytania: {milisec}ms')
    return wrapper


@get_res_time
def get_res():
    url = "https://api.exchangeratesapi.io/latest"
    base_currency = 'EUR'
    params = {'base': base_currency}
    try:
        res = requests.get(url, params)
        print(extract_eur_to_pln(res.json()))
        print(get_datetime())
        return res
    except TimeoutError:
        print("Response time from endpoint was too long.")


def extract_eur_to_pln(response_json):
    currency_data = response_json["rates"]
    return f'Kurs EUR {currency_data["PLN"]}'


while True:
    if datetime.now().second % 15 == 0:
        print('----------------------------------------------')
        get_res()
        print('----------------------------------------------')
        time.sleep(1)
