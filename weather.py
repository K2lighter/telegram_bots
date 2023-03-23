import telebot
import requests
import json

bot = telebot.TeleBot('6065480166:AAFOiymj_jPL51uejmLmoRZmqwVtUb9LjWw')
API = '38d5adbb4732079062e9349650029f47'
url = 'https://api.openweathermap.org/data/2.5/weather?q=Seattle&appid=38d5adbb4732079062e9349650029f47&units=metric'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])  # отслеживаем именно текст(не видео, не аудио)
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Температура воздуха в городе {city} равна {round(temp)} градусов цельсия')
        image = 'sun.jpg' if temp > 5.0 else 'cloud.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Вы ввели несуществующий город')


bot.polling(none_stop=True)
