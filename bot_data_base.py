import telebot
import sqlite3

bot = telebot.TeleBot("6065480166:AAFOiymj_jPL51uejmLmoRZmqwVtUb9LjWw")
name = None


@bot.message_handler(commands=['start'])
def start(message):
    con = sqlite3.connect('lighter.sql')
    cur = con.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(21), password varchar(21))')

    con.commit()
    cur.close()
    con.close()

    bot.send_message(message.chat.id, 'Привет, сейчас я тебя зарегистрирую, введи ваше имя')
    bot.register_next_step_handler(message, user_name)  # вызывает следующую функцию


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    password = message.text.strip()
    con = sqlite3.connect('lighter.sql')
    cur = con.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    con.commit()
    cur.close()
    con.close()
    markup = telebot.types.InlineKeyboardMarkup()  # для кнопки
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    con = sqlite3.connect('lighter.sql')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ''
    for elem in users:
        info += f'Имя: {elem[1]}, Пароль: {elem[2]}\n'
    cur.close()
    con.close()
    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
