from os.path import join
import requests
import json
from getpass import getpass

# Поиск местонахождения для запросов  к  курсам ПриватБанка
response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5' )


if response.status_code == 200:
    print('Success, Connect!')
elif response.status_code == 404:
    print('Not Found.')
# Анализ некоторых атрибутов местонахождения запросов
response_json = response.json()
# print(response.headers)
# print(response_json)

for i in  response_json:
    print(i)

