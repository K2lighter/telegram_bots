# работа с файлами и создание кнопок
import telebot
from telebot import types

bot = telebot.TeleBot('6065480166:AAFOiymj_jPL51uejmLmoRZmqwVtUb9LjWw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт 😂')
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn1)  # одна кнопка в ряду
    markup.row(btn2, btn3)  # две кнопки в ряду
    file = open('./DSC09223.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    audio = open('./45_mobile-rington.mp3', 'rb')
    bot.send_audio(message.chat.id, audio, reply_markup=markup)
    video = open("C:\\Users\\k2lig\\Downloads\\Telegram Desktop\\video_2023-03-22_10-51-59.mp4", 'rb')
    bot.send_video(message.chat.id, video, reply_markup=markup)
    bot.send_message(message.chat.id, 'Привет, медвед', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Удалить все к херам')


@bot.message_handler(content_types=['photo'])  # можно в список положить любой файл audio, video
def get_photo(message):
    """
    Функция при отправке фото будет отвечать 'Какое красивое фото', создавать кнопки
    с переходом на сайт гугл
    удалить фото
    изменить текст
    """
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1)  # одна кнопка в ряду
    markup.row(btn2, btn3)  # две кнопки в ряду
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


@bot.message_handler(content_types=['video'])  # можно в список положить любой файл audio, video
def get_photo(message):
    bot.reply_to(message, 'Какое классное видео')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit_text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)  # программа будет работать постоянно
