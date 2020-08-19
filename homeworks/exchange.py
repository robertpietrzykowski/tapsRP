import csv
import functools
import requests
import time
from datetime import datetime


def get_datetime():
    actual_time = datetime.now()
    formatted_time = actual_time.strftime("%d.%m.%Y %H:%M:%S")
    return formatted_time


def get_res_time(res):
    @functools.wraps(res)
    def wrapper(*args, **kwargs):
        milisec = int(res().elapsed.microseconds * 0.001)
        return milisec
    return wrapper


@get_res_time
def get_res():
    url = "https://api.exchangeratesapi.io/latest"
    base_currency = 'EUR'
    params = {'base': base_currency}
    try:
        res = requests.get(url, params)
        miliseconds = int(res.elapsed.microseconds * 0.001)
        print(f'Kurs EUR {extract_eur_to_pln(res.json())}')
        print(f'Data i godzina: {get_datetime()}')
        print(f'Czas wykonania zapytania: {miliseconds} ms')
        write_to_csv(extract_eur_to_pln(res.json()), get_datetime(), miliseconds)
        return res
    except TimeoutError:
        print("Response time from endpoint was too long.")


def extract_eur_to_pln(response_json):
    currency_data = response_json["rates"]
    return currency_data["PLN"]


def write_to_csv(rate, date_time, request_time):
    with open('exchange.csv', mode='a') as exchange_file:
        fieldnames = ['Kurs EUR', 'Data i Godzina', 'Czas wykonania']
        exchange_writer = csv.DictWriter(exchange_file, fieldnames=fieldnames)
        exchange_writer.writerow({'Kurs EUR': rate, 'Data i Godzina':date_time, 'Czas wykonania': request_time})


while True:
    # if datetime.now().second % 15 == 0:
        print('----------------------------------------------')
        get_res()
        print('----------------------------------------------')
        time.sleep(1)
