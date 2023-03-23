# pip install pyTelegramBotApi
import telebot
import webbrowser

bot = telebot.TeleBot('6065480166:AAFOiymj_jPL51uejmLmoRZmqwVtUb9LjWw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, медвед')
    # вызов в телеграм /start


@bot.message_handler(commands=['help'])
def main(message):
    """Применяем html для текста"""
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>Помощь когда-нибудь будет</u></em>', parse_mode='html')
    # вызов в телеграм /help


@bot.message_handler(commands=['user_info'])
def main(message):
    """Выведем всю информацию о пользователе"""
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['user'])
def main(message):
    """Выведем некоторую информацию о пользователе"""
    bot.send_message(message.chat.id, f'{message.from_user.first_name} - ты красавчик')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    """
    Функция открывает сайт
    """
    webbrowser.open('https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%B8%D0%BD%D0%B1%D0%B0%D0%B5%D0%B2%D0%B0,_%D0%95%D0%BB%D0%B5%D0%BD%D0%B0_%D0%93%D0%B0%D0%B4%D0%B6%D0%B8%D0%B5%D0%B2%D0%BD%D0%B0')


@bot.message_handler()
def info(message):
    """
    Функция без параметров вызывается либо после функций
    иначе код после не выполнится
    """

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'{message.from_user.first_name} - ты красавчик')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')  # выдает в виде ответа на сообщение


bot.polling(none_stop=True)  # программа будет работать постоянно
# bot.infinity_polling() # делает тоже самое
