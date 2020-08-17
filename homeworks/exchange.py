import requests
from datetime import datetime
import time


def get_response_time_and_datetime(fn):
    def wrapper():
        actual_time = datetime.now()
        formatted_time = actual_time.strftime("%d.%m.%Y %H:%M:%S")
        milisec = int(fn().elapsed.microseconds * 0.001)
        print(f'Data i godzina: {formatted_time}')
        print(f'Czas wykonania zapytania: {milisec}ms')
    return wrapper


@get_response_time_and_datetime
def get_res():
    url = "https://api.exchangeratesapi.io/latest"
    base_currency = 'EUR'
    try:
        params = {'base': base_currency}
        res = requests.get(url, params)
        print(extract_eur_to_pln(res.json()))
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









# def get_actual_data_and_time(get_data):
#     def get_datetime():
#         actual_time = datetime.now()
#         formatted_time = actual_time.strftime("%d.%m.%Y %H:%M:%S")
#         print(formatted_time)
#         get_data()
#         return get_datetime
#
#
# @get_actual_data_and_time
# def get_exchange_data():
#     url = "https://api.exchangeratesapi.io/latest"
#     base_currency = 'EUR'
#     try:
#         params = {'base': base_currency}
#         res = requests.get(url, params)
#         print(extract_eur_to_pln(res.json()))
#         print(get_response_time(res))
#         return res
#     except TimeoutError:
#         print("Response time from endpoint was too long.")
#
#
# def extract_eur_to_pln(response_json):
#     currency_data = response_json["rates"]
#     return f'Kurs EUR {currency_data["PLN"]}'
#
#
# def get_response_time(response):
#     milisec = int(response.elapsed.microseconds * 0.001)
#     return f'Czas wykonania zapytania: {milisec}ms'
#
#
#
#
#
#
# while True:
#     # if datetime.now().second % 15 == 0:
#         print('----------------------------------------------')
#         get_exchange_data()
#         print('----------------------------------------------')
#         time.sleep(1)
