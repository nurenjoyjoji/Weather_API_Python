import requests
from pprint import pprint
from datetime import datetime
def weather(API,city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    response = requests.get(url)
    data = response.json()
    sunrise = datetime.fromtimestamp(data["sys"]['sunrise'])
    sunset = datetime.fromtimestamp(data["sys"]['sunset'])
    return f""""
Город: {data["name"]}
Температура: {data["main"]["temp"]}
Давление: {data["main"]["pressure"]}
Влажность: {data["main"]["humidity"]}
Скорость ветра: {data["wind"]["speed"]}
Погода: {data["weather"][0]["description"]}
Восход солнце: {sunrise.time()}
Продол. дня: {sunset - sunrise}
Закат солнце: {sunset.time()}
"""
while True:
    try:
        city = input("ВВедите название города или Exit : ")
        API = "f79bd8676437b40dbd8b56cf03c1f75c"
        if city == "Exit":
            break
        else:
            print(weather(API , city))
        print(weather(API , city))
    except Exception:
        print("Город не существует")
        break