import telebot
from telebot import types as t
from random import randint as r
import time
from бот.saiti import *

token = '5288890666:AAEmueoSm0JoNpaIferVH95EmepzclvGfBk'
bot = telebot.TeleBot(token)

privet = ['q', 'qq', 'hi', 'hello', 'privet', 'sup', 'what\'s up',  'здравствуйте', 'хай', 'ghbdtn', 'plfhjdf', 'здарова', 'привет']

@bot.message_handler(commands=['start', 'help'])
def knopki(message):
    m = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = t.KeyboardButton('💹 Курс валют к рублю')
    b2 = t.KeyboardButton('☂ Погода в ЧГ')
    b3 = t.KeyboardButton('🕰 Точное время в разных частях света ')
    b4 = t.KeyboardButton('🎲 Рандомное число')
    m.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Главное меню 🖼', reply_markup=m)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() in privet:
        bot.send_message(message.chat.id, f'И тебе привет, {message.from_user.first_name}!')
        bot.send_sticker(message.chat.id, open('../3.webp', 'rb'))
    if message.text == '🎲 Рандомное число':
        bot.send_message(message.chat.id, '1..')
        time.sleep(0.2)
        bot.send_message(message.chat.id, '2..')
        time.sleep(0.2)
        bot.send_message(message.chat.id, '3..')
        time.sleep(0.3)
        bot.send_message(message.chat.id, str(r(0, 10**4)))
    if message.text == '💹 Курс валют к рублю':
        ma = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bu1 = t.KeyboardButton('💵 Курс доллара')
        bu2 = t.KeyboardButton('💶 Курс евро')
        bu3 = t.KeyboardButton('¥ Курс юаня')
        bu4 = t.KeyboardButton('⧫ Курс ethereum')
        bu5 = t.KeyboardButton('₿ Курс bitcoin')
        bu6 = t.KeyboardButton('💷 Курс фунт стерлингов')
        bu7 = t.KeyboardButton('Back 🔙')
        ma.add(bu1, bu2, bu3, bu6,  bu4, bu5, bu7)
        bot.send_message(message.chat.id, 'Выберите нужную валюту 👇', reply_markup=ma)
    if message.text == '☂ Погода в ЧГ':
        bot.send_message(message.chat.id, glob_pog)
    if message.text == '💵 Курс доллара':
        bot.send_message(message.chat.id, f'Курс: {convert[0].text} рублей к доллару')
    if message.text == '💶 Курс евро':
        bot.send_message(message.chat.id, f'Курс: {convert2[0].text} рублей к евро')
    if message.text == '¥ Курс юаня':
        bot.send_message(message.chat.id, f'Курс: {convert3[0].text} рублей к юаню')
    if message.text == '⧫ Курс ethereum':
        bot.send_message(message.chat.id, eth)
    if message.text == '₿ Курс bitcoin':
        bot.send_message(message.chat.id, btc)
    if message.text == '💷 Курс фунт стерлингов':
        bot.send_message(message.chat.id, f'Курс: {convert4[0].text} рублей к фунту стерлингов')
    if message.text == 'Back 🔙':
        knopki(message)
    if message.text.lower() == 'подтвердить' and message.chat.id == 412569566:
        bot.send_message(412569566, 'Cool!')

bot.polling(none_stop=True)
