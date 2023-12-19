import faker
import telebot
from telebot import types as t
import sqlite3 as sql
from faker import Faker
from string import ascii_lowercase, ascii_uppercase, digits


fake = faker.Faker()
token = '6679877578:AAGFjB8HPqIYCi1Agth2w3vdtzg0VZay6sQ'
bot = telebot.TeleBot(token)


user = ''
owner, buyer = False, False
login, password = '', ''
city, street, house, metro, rooms, price, area, floor, apts, lena, nomer = '', '', '', 0, 0, 0, 0, 0, [], 0, 0

is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor = False, False, False, False, False, False, False, False
registration, authorization, working = False, False, False
reg_log, reg_passw, reg_end = False, False, False
auth_log, auth_passw, auth_end = False, False, False
adding, information, activity, searching = False, False, False, False
changing, watching, inf_about = False, False, False
changing_1, changing_2, filtering = False, False, False
fio, number, email, zapros, nomer_poiska = '', '', '', [], 0
is_fio, is_number, is_email, is_zapros = False, False, False, False
vpered, nazad, domoy, sorting, reverse_sorting = False, False, False, False, False
owner_data = []
b_menu = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
poisk = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
back_ = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    m = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = t.KeyboardButton('Зарегистрироваться')
    b2 = t.KeyboardButton('Войти')
    m.add(b1, b2)
    bot.send_message(message.chat.id, 'Привет, меня зовут Борис. Мой профиль - квартирный вопрос, '
                                      'погубивший москвичей ещё в 20-ом веке, по версии Булгакова. '
                                      'В эпоху современных технологий таких проблем не будет. '
                                      'Я помогу вам быстро найти необходимую информацию по покупке/продаже квартиры.')
    bot.send_message(message.chat.id, 'В первую очередь вам необходимо зарегистрироваться '
                                      'или войти в уже существующий профиль.', reply_markup=m)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global user, authorization, registration, working, owner, buyer, \
        login, password, city, street, house, metro, rooms, price, area, floor, \
        reg_log, reg_passw, reg_end, auth_log, auth_passw, auth_end, appartametns, \
        adding, information, activity, searching, changing, watching, inf_about, zapros, \
        is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor, apts, \
        lena, changing_1, changing_2, nomer, fio, number, email, is_fio, is_number, is_email, \
        is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor, \
        filtering, is_zapros, nomer_poiska, vpered, nazad, domoy, sorting, reverse_sorting, owner_data, b_menu, poisk, back_
    connection = sql.connect(r'C:\Users\liubo\OneDrive\Документы\Skillbox_SQLite_Webinar-master\SQLiteStudio\bd_agency')
    cursor = connection.cursor()
    owner_data = cursor.execute(f'SELECT * FROM owners').fetchall()
    if call.data == "Москва":
        bot.send_message(user, "Выбран город Москва", reply_markup=back_)
        city = "Москва"
        if owner:
            bot.send_message(user, "Введите улицу")
            is_street = True
        elif buyer:
            bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
            is_metro = True
    elif call.data == "Нижний Новгород":
        bot.send_message(user, "Выбран город Нижний Новгород", reply_markup=back_)
        city = "Нижний Новгород"
        if owner:
            bot.send_message(user, "Введите улицу")
            is_street = True
        elif buyer:
            bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
            is_metro = True
    elif call.data == "Новосибирск":
        bot.send_message(user, "Выбран город Новосибирск", reply_markup=back_)
        city = "Новосибирск"
        if owner:
            bot.send_message(user, "Введите улицу")
            is_street = True
        elif buyer:
            bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
            is_metro = True
    elif call.data == "Казань":
        bot.send_message(user, "Выбран город Казань", reply_markup=back_)
        city = "Казань"
        if owner:
            bot.send_message(user, "Введите улицу")
            is_street = True
        elif buyer:
            bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
            is_metro = True
    elif call.data == "Санкт-Петербург":
        bot.send_message(user, "Выбран город Санкт-Петербург", reply_markup=back_)
        city = "Санкт-Петербург"
        if owner:
            bot.send_message(user, "Введите улицу")
            is_street = True
        elif buyer:
            bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
            is_metro = True
    elif call.data == "cb_yes":
        bot.send_message(user, "Цены отсортированы по возрастанию")
        zapros = cursor.execute(f'SELECT * FROM apts'
                                + (f' WHERE a_city = "{city}"')
                                + (f' AND a_metro BETWEEN {int(metro) - 500} AND {int(metro) + 500}')
                                + (f' AND a_rooms = {rooms}')
                                + (f' AND a_price BETWEEN {int(price) * 0.9} AND {int(price) * 1.1}')
                                + (f' AND a_area BETWEEN {int(area) * 0.9} AND {int(area) * 1.1}')
                                # + (f' AND a_floor BETWEEN {int(floor) * 0.9} AND {int(floor) * 1.1}' if int(floor) != 0 else "")
                                + (f' ORDER BY a_price')).fetchall()
                                # + (f' ORDER BY a_price DESC' if reverse_sorting else "")).fetchall()
        print(zapros)
        if len(zapros) == 0:
            bot.send_message(user, "Нет квартир с данными параметрами", reply_markup=b_menu)
            vpered, nazad = False, False
            nomer_poiska = 0
            filtering, is_zapros, city, street, house, metro, rooms, price, area, floor, domoy = False, False, '', '', '', 0, 0, 0, 0, 0, False
        else:
            bot.send_message(user, f'Квартира по адресу: {zapros[nomer_poiska][2]}, '
                                   f'{zapros[nomer_poiska][3]}, {zapros[nomer_poiska][4]} '
                                   f'\nНаходится на {zapros[nomer_poiska][9]} этаже в {zapros[nomer_poiska][5]} метрах от'
                                   f' ближайшего метро \nКоличество комнат: {zapros[nomer_poiska][6]} '
                                   f'\nПлощадь (в квадратных метрах): {zapros[nomer_poiska][8]} '
                                   f'\nЦена (в рублях): {zapros[nomer_poiska][7]}\n'
                                   f'Владелец: ' + str(
                owner_data[nomer_poiska][1] if len(owner_data[nomer_poiska][1]) != 0 else "Не указан")
                             + "\nКонтактный номер: " + str(
                owner_data[nomer_poiska][2] if len(owner_data[nomer_poiska][2]) != 0 else "Не указан")
                             + "\nПочта владельца: " + str(
                owner_data[nomer_poiska][3] if len(owner_data[nomer_poiska][3]) != 0 else "Не указан"),
                             reply_markup=poisk)
            vpered = True
            is_zapros = True

    elif call.data == "cb_no":
        bot.send_message(user, "Цены отсортированы по убыванию")
        zapros = cursor.execute(f'SELECT * FROM apts'
                                + (f' WHERE a_city = "{city}"')
                                + (f' AND a_metro BETWEEN {int(metro) - 500} AND {int(metro) + 500}')
                                + (f' AND a_rooms = {rooms}')
                                + (f' AND a_price BETWEEN {int(price) * 0.9} AND {int(price) * 1.1}')
                                + (f' AND a_area BETWEEN {int(area) * 0.9} AND {int(area) * 1.1}')
                                # + (f' AND a_floor BETWEEN {int(floor) * 0.9} AND {int(floor) * 1.1}' if int(floor) != 0 else "")
                                # + (f' ORDER BY a_price' if sorting else "")
                                + (f' ORDER BY a_price DESC')).fetchall()
        print(zapros)
        if len(zapros) == 0:
            bot.send_message(user, "Нет квартир с данными параметрами", reply_markup=b_menu)
            vpered, nazad = False, False
            nomer_poiska = 0
            filtering, is_zapros, city, street, house, metro, rooms, price, area, floor, domoy = False, False, '', '', '', 0, 0, 0, 0, 0, False
        else:
            bot.send_message(user, f'Квартира по адресу: {zapros[nomer_poiska][2]}, '
                                   f'{zapros[nomer_poiska][3]}, {zapros[nomer_poiska][4]} '
                                   f'\nНаходится на {zapros[nomer_poiska][9]} этаже в {zapros[nomer_poiska][5]} метрах от'
                                   f' ближайшего метро \nКоличество комнат: {zapros[nomer_poiska][6]} '
                                   f'\nПлощадь (в квадратных метрах): {zapros[nomer_poiska][8]} '
                                   f'\nЦена (в рублях): {zapros[nomer_poiska][7]}\n'
                                   f'Владелец: ' + str(
                owner_data[nomer_poiska][1] if len(owner_data[nomer_poiska][1]) != 0 else "Не указан")
                             + "\nКонтактный номер: " + str(
                owner_data[nomer_poiska][2] if len(owner_data[nomer_poiska][2]) != 0 else "Не указан")
                             + "\nПочта владельца: " + str(
                owner_data[nomer_poiska][3] if len(owner_data[nomer_poiska][3]) != 0 else "Не указан"),
                             reply_markup=poisk)
            vpered = True
            is_zapros = True
    elif call.data == "cb_skip":
        bot.send_message(user, "Результат поиска")
        zapros = cursor.execute(f'SELECT * FROM apts'
                                + (f' WHERE a_city = "{city}"')
                                + (f' AND a_metro BETWEEN {int(metro) - 500} AND {int(metro) + 500}')
                                + (f' AND a_rooms = {rooms}')
                                + (f' AND a_price BETWEEN {int(price) * 0.9} AND {int(price) * 1.1}')
                                + (f' AND a_area BETWEEN {int(area) * 0.9} AND {int(area) * 1.1}')).fetchall()
        print(zapros)
        if len(zapros) == 0:
            bot.send_message(user, "Нет квартир с данными параметрами", reply_markup=b_menu)
            vpered, nazad = False, False
            nomer_poiska = 0
            filtering, is_zapros, city, street, house, metro, rooms, price, area, floor, domoy = False, False, '', '', '', 0, 0, 0, 0, 0, False
        else:
            bot.send_message(user, f'Квартира по адресу: {zapros[nomer_poiska][2]}, '
                                   f'{zapros[nomer_poiska][3]}, {zapros[nomer_poiska][4]} '
                                   f'\nНаходится на {zapros[nomer_poiska][9]} этаже в {zapros[nomer_poiska][5]} метрах от'
                                   f' ближайшего метро \nКоличество комнат: {zapros[nomer_poiska][6]} '
                                   f'\nПлощадь (в квадратных метрах): {zapros[nomer_poiska][8]} '
                                   f'\nЦена (в рублях): {zapros[nomer_poiska][7]}\n'
                                   f'Владелец: ' + str(
                owner_data[nomer_poiska][1] if len(owner_data[nomer_poiska][1]) != 0 else "Не указан")
                             + "\nКонтактный номер: " + str(
                owner_data[nomer_poiska][2] if len(owner_data[nomer_poiska][2]) != 0 else "Не указан")
                             + "\nПочта владельца: " + str(
                owner_data[nomer_poiska][3] if len(owner_data[nomer_poiska][3]) != 0 else "Не указан"),
                             reply_markup=poisk)
            vpered = True
            is_zapros = True

@bot.message_handler(content_types=['text'])
def send_message(message):
    connection = sql.connect(r'C:\Users\liubo\OneDrive\Документы\Skillbox_SQLite_Webinar-master\SQLiteStudio\bd_agency')
    cursor = connection.cursor()

    global user, authorization, registration, working, owner, buyer, \
        login, password, city, street, house, metro, rooms, price, area, floor, \
        reg_log, reg_passw, reg_end, auth_log, auth_passw, auth_end, appartametns, \
        adding, information, activity, searching, changing, watching, inf_about, zapros, \
        is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor, apts, \
        lena, changing_1, changing_2, nomer, fio, number, email, is_fio, is_number, is_email, \
        is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor, \
        filtering, is_zapros, nomer_poiska, vpered, nazad, domoy, sorting, reverse_sorting, owner_data, b_menu, poisk, back_

    user, sms = message.chat.id, message.text
    passwords = [sim[0] for sim in cursor.execute(f'SELECT password FROM people').fetchall()]
    logins = [sim[0] for sim in cursor.execute(f'SELECT login FROM people').fetchall()]

    reg = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    reg_1 = t.KeyboardButton('Я владелец')
    reg_2 = t.KeyboardButton('Я покупатель')
    reg_3 = t.KeyboardButton('Назад')
    reg.add(reg_1, reg_2, reg_3)

    menu = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu_1 = t.KeyboardButton('Зарегистрироваться')
    menu_2 = t.KeyboardButton('Войти')
    menu.add(menu_1, menu_2)

    back = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back_1 = t.KeyboardButton('Назад')
    back.add(back_1)

    back_ = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back_1_ = t.KeyboardButton('Меню')
    back_.add(back_1_)

    b_menu = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b_menu_1 = t.KeyboardButton('Посмотреть варианты квартир')
    b_menu_2 = t.KeyboardButton('Добавить информацию о себе')
    b_menu_3 = t.KeyboardButton('Сменить пользователя/выйти')
    b_menu.add(b_menu_1, b_menu_2, b_menu_3)

    o_menu = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    o_menu_1 = t.KeyboardButton('Информация о квартире')
    o_menu_2 = t.KeyboardButton('Добавить квартиру')
    o_menu_3 = t.KeyboardButton('Добавить информацию о себе')
    o_menu_4 = t.KeyboardButton('Сменить пользователя/выйти')
    o_menu.add(o_menu_1, o_menu_2, o_menu_3, o_menu_4)

    poisk = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    poisk_1 = t.KeyboardButton('Назад')
    poisk_2 = t.KeyboardButton('Вперед')
    poisk_3 = t.KeyboardButton('Меню')
    poisk.add(poisk_1, poisk_2, poisk_3)

    filt = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    filt_1 = t.KeyboardButton('Город')
    filt_2 = t.KeyboardButton('Улица')
    filt_3 = t.KeyboardButton('Дом')
    filt_4 = t.KeyboardButton('Расстояние до метро')
    filt_5 = t.KeyboardButton('Количество комнат')
    filt_6 = t.KeyboardButton('Цена')
    filt_7 = t.KeyboardButton('Площадь')
    filt_8 = t.KeyboardButton('Этаж')
    filt_9 = t.KeyboardButton('Отсортировать цены по возрастанию')
    filt_10 = t.KeyboardButton('Отсортировать цены по убыванию')
    filt_11 = t.KeyboardButton('Поиск')
    filt_12 = t.KeyboardButton('Меню')
    filt.add(filt_1, filt_2, filt_3, filt_4, filt_5, filt_6, filt_7, filt_8, filt_9, filt_10, filt_11, filt_12)

    gorod = t.InlineKeyboardMarkup(row_width=3)
    gorod_1 = t.InlineKeyboardButton("Москва", callback_data="Москва")
    gorod_2 = t.InlineKeyboardButton("Санкт-Петербург", callback_data="Санкт-Петербург")
    gorod_3 = t.InlineKeyboardButton("Нижний Новгород", callback_data="Нижний Новгород")
    gorod_4 = t.InlineKeyboardButton("Новосибирск", callback_data="Новосибирск")
    gorod_5 = t.InlineKeyboardButton("Казань", callback_data="Казань")
    gorod.add(gorod_1, gorod_2, gorod_3, gorod_4, gorod_5)

    inmarkup = t.InlineKeyboardMarkup(row_width=3)
    inmarkup.add(t.InlineKeyboardButton("Отсортировать цены по возрастанию", callback_data="cb_yes"),
               t.InlineKeyboardButton("Отсортировать цены по убыванию", callback_data="cb_no"),
               t.InlineKeyboardButton("Пропустить", callback_data="cb_skip"))

    infa = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    infa_1 = t.KeyboardButton('Изменить цену')
    infa_2 = t.KeyboardButton('Посмотреть информацию о квартире')
    infa_3 = t.KeyboardButton('Меню')
    infa.add(infa_1, infa_2, infa_3)

    if registration:

        if sms == 'Назад':
            bot.send_message(user, 'В первую очередь вам необходимо '
                                   'зарегистрироваться или войти в уже существующий профиль.', reply_markup=menu)
            registration, reg_log, reg_passw, reg_end = False, False, False, False
            login, password, owner, buyer = '', '', False, False

        if reg_end:
            password = sms
            k = 0

            if (set(password).intersection(set(ascii_uppercase))
                    and set(password).intersection(set(ascii_lowercase))
                    and set(password).intersection(set(digits))) and len(password) >= 8 and len(password) <= 24:
                for sim in password:
                    if sim in digits + ascii_uppercase + ascii_lowercase:
                        pass
                    else:
                        bot.send_message(user, "Ваш пароль должен содержать от 8 до 24 символов и "
                                               "включать в себя строчные и заглавные латинские буквы, а также цифры. Попробуйте еще раз.")
                        k = 1
                        break
                if k == 0:
                    reg_end, registration, working = False, False, True
                    cursor.execute(
                        f'INSERT INTO people (login, password, buy_own) VALUES ("{login}", "{password}", {owner == True})')
                    if owner:
                        bot.send_message(user, 'Регистрация прошла успешно!\nВыберите интересующий'
                                               ' Вас запрос:', reply_markup=o_menu)
                        cursor.execute(f'INSERT INTO owners (o_login) VALUES ("{login}")')
                    elif buyer:
                        bot.send_message(user, 'Регистрация прошла успешно!\nВыберите интересующий'
                                               ' Вас запрос:', reply_markup=b_menu)
                        cursor.execute(f'INSERT INTO buyers (b_login) VALUES ("{login}")')

            else:
                bot.send_message(user, "Ваш пароль должен содержать от 8 до 24 символов и "
                                       "включать в себя строчные и заглавные латинские буквы, а также цифры. Попробуйте еще раз.")
        if reg_passw:
            login = sms
            l = 0
            for sim in login:
                if sim in digits + ascii_uppercase + ascii_lowercase:
                    pass
                else:
                    l = 1
                    break
            if l == 0:
                if login in logins:
                    bot.send_message(user, 'Данный логин уже занят, попробуйте другой')
                else:
                    bot.send_message(user, 'Придумайте пароль')
                    reg_passw, reg_end = False, True
            else:
                bot.send_message(user,"Логин должен содержать латинские буквы, а также может включать цифры. \nПопробуйте еще раз")

        if reg_log:
            if sms == 'Я владелец' or sms == 'Я покупатель':
                bot.send_message(user, 'Придумайте логин\nОн должен содержать только латинские буквы, а также может включать цифры', reply_markup=back)
                if sms == 'Я владелец':
                    owner = True
                    reg_log, reg_passw = False, True
                elif sms == 'Я покупатель':
                    buyer = True
                    reg_log, reg_passw = False, True
            else:
                bot.send_message(user, 'Выберите существующую опцию')


    elif authorization:

        if sms == 'Назад':
            bot.send_message(user, 'В первую очередь вам необходимо '
                                   'зарегистрироваться или войти в уже существующий профиль.', reply_markup=menu)
            authorization, auth_log, auth_passw, auth_end = False, False, False, False
            login, password, buyer, owner = '', '', False, False

        if auth_end:
            password = sms
            password_db = cursor.execute(f'SELECT password FROM people WHERE login = "{login}"').fetchall()[0][0]
            owbu = cursor.execute(f'SELECT buy_own FROM people WHERE login = "{login}"').fetchall()[0][0]
            if password == password_db:
                working = True
                if owbu == True:
                    bot.send_message(user, 'Авторизация успешна', reply_markup=o_menu)
                    owner = True
                elif owbu == False:
                    bot.send_message(user, 'Авторизация успешна', reply_markup=b_menu)
                    buyer = True
                auth_end, authorization = False, False
            else:
                bot.send_message(user, 'Введен неверный пароль, попробуйте ещё раз')

        if auth_passw:
            login = sms
            if login in logins:
                bot.send_message(user, 'Введите пароль')
                auth_passw, auth_end = False, True
            else:
                bot.send_message(user, 'Данного логина не существует, попробуйте ещё раз')


    elif working:

        if owner:

            if adding:
                if sms == 'Назад':
                    bot.send_message(user, 'Выберите действие', reply_markup=o_menu)
                    adding, information, activity, searching = False, False, False, False
                    is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor = False, False, False, False, False, False, False, False
                    city, street, house, metro, rooms, price, area, floor = '', '', '', 0, 0, 0, 0, 0

                elif is_city:
                    city = sms
                    is_city, is_street = False, True
                    bot.send_message(user, 'Введите улицу')
                elif is_street:
                    street = sms
                    is_street, is_house = False, True
                    bot.send_message(user, 'Введите дом')
                elif is_house:
                    house = sms
                    is_house, is_metro = False, True
                    bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
                elif is_metro:
                    metro = sms
                    is_metro, is_rooms = False, True
                    bot.send_message(user, 'Введите количество комнат в квартире')
                elif is_rooms:
                    rooms = sms
                    is_rooms, is_price = False, True
                    bot.send_message(user, 'Введите цену за квартиру (в рублях)')
                elif is_price:
                    price = sms
                    is_price, is_area = False, True
                    bot.send_message(user, 'Введите площадь квартиры (в квадратных метрах)')
                elif is_area:
                    area = sms
                    is_area, is_floor = False, True
                    bot.send_message(user, 'Введите этаж квартиры')
                elif is_floor:
                    floor = sms
                    is_floor, adding = False, False
                    cursor.execute(f'INSERT INTO apts (o_login, a_city, a_street, a_house, a_metro, a_rooms, a_price, '
                                   f'a_area, a_floor) VALUES ("{login}", "{city}", "{street}", "{house}", '
                                   f'"{metro}", "{rooms}", "{price}", "{area}", "{floor}")')
                    city, street, house, metro, rooms, price, area, floor = '', '', '', 0, 0, 0, 0, 0
                    bot.send_message(user, 'Успешно добавлено', reply_markup=o_menu)

            elif inf_about:
                if sms == 'Назад':
                    bot.send_message(user, 'Выберите действие', reply_markup=o_menu)
                    email, number, fio, is_email, is_number, is_fio, inf_about = '', '', '', False, False, False, False
                elif is_fio:
                    fio = sms
                    bot.send_message(user, 'Введите свой номер')
                    is_fio, is_number = False, True

                elif is_number:
                    number = sms
                    bot.send_message(user, 'Введите свою почту')
                    is_number, is_email = False, True

                elif is_email:
                    email = sms
                    cursor.execute(f'UPDATE owners SET o_fio = "{fio}", o_number = "{number}", o_email = "{email}" WHERE o_login = "{login}"')
                    bot.send_message(user, 'Информация успешно добавлена', reply_markup=o_menu)
                    is_email, inf_about = False, False
                    fio, number, email = '', '', ''

            elif changing:

                if changing_1:
                    try:
                        nomer = sms
                        if int(nomer) in [sim for sim in range(1, lena + 1)]:
                            changing_1, changing_2 = False, True
                            bot.send_message(user, "Введите новую цену", reply_markup=back)
                        else:
                            bot.send_message(user, "Выберите квартиру в меню")
                            for i in range(lena):
                                bot.send_message(user, f"{i + 1}) {apts[i][2]}")
                    except ValueError:
                        bot.send_message(user, "Выберите квартиру в меню")
                        for i in range(lena):
                            bot.send_message(user, f"{i+1}) {apts[i][2]}")
                elif changing_2:
                    try:
                        new_price = sms
                        cursor.execute(f'UPDATE apts SET a_price = {int(new_price)} WHERE o_login = "{login}" '
                                       f'AND a_city = "{apts[int(nomer)-1][2]}" AND a_street = '
                                       f'"{apts[int(nomer)-1][3]}" AND a_house = "{apts[int(nomer)-1][4]}"')
                        bot.send_message(user, 'Успешно изменено', reply_markup=o_menu)
                        changing_2, changing = False, False
                        new_price, nomer = 0, 0
                    except ValueError:
                        bot.send_message(user, "Вы ввели не число")

            elif information:

                apts = cursor.execute(f'SELECT * FROM apts WHERE o_login = "{login}"').fetchall()
                lena = len(apts)
                if sms == 'Назад':
                    bot.send_message(user, 'Выберите действие', reply_markup=o_menu)
                    adding, information, activity, searching = False, False, False, False

                elif sms == 'Изменить цену':
                    if lena == 0:
                        bot.send_message(user, "У вас нет добавленных квартир, чтобы изменить цену", reply_markup=o_menu)
                        adding, information, activity, searching = False, False, False, False
                    else:
                        changing, information, changing_1 = True, False, True
                        cifri = (t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=lena + 1))

                        for i in range(lena):
                            cifri.add(t.KeyboardButton(f"{i + 1}"))
                        bot.send_message(user, "Выберите квартиру", reply_markup=cifri)
                        for i in range(lena):
                            bot.send_message(user, f"{i+1}) {apts[i][2]}")

                elif sms == 'Посмотреть информацию о квартире':
                    if lena == 0:
                        bot.send_message(user, 'У вас не добавлено ни одной квартиры', reply_markup=o_menu)
                    else:
                        for i in range(lena):
                            city, street, house, metro, rooms, price, area, floor = apts[i][2:]
                            bot.send_message(user, f'Ваша квартира по адресу: {city}, {street}, {house} '
                                                   f'\nНаходится на {floor} этаже в {metro} метрах от'
                                                   f' ближайшего метро \nКоличество комнат: {rooms} '
                                                   f'\nПлощадь (в квадратных метрах):{area} '
                                                   f'\nЦена (в рублях): {price}', reply_markup=o_menu)
                    information = False

                else:
                    bot.send_message(user, 'Выберите существующее действие')

            elif sms == 'Сменить пользователя/выйти':
                bot.send_message(user, 'В первую очередь вам необходимо '
                                       'зарегистрироваться или войти в уже существующий профиль.', reply_markup=menu)
                working, owner = False, False
                adding, changing, inf_about, information = False, False, False, False
                activity, searching = False, False
                is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor = False, False, False, False, False, False, False, False
                city, street, house, metro, rooms, price, area, floor = '', '', '', 0, 0, 0, 0, 0
                is_email, inf_about = False, False
                fio, number, email, login, password = '', '', '', '', ''
                changing_2, changing = False, False
                new_price, nomer = 0, 0

            elif sms == 'Меню':
                adding, information, activity, searching = False, False, False, False
                bot.send_message(user, 'Выберите действие', reply_markup=o_menu)

            elif sms == 'Добавить информацию о себе':
                bot.send_message(user, 'Введите свое ФИО', reply_markup=back)
                inf_about, is_fio = True, True

            elif sms == 'Добавить квартиру':
                adding, is_city = True, True
                bot.send_message(user, 'Введите город', reply_markup=back)

            elif sms == 'Информация о квартире':
                information = True
                bot.send_message(user, "Выберите действие", reply_markup=infa)


        if buyer:

            if sms == 'Сменить пользователя/выйти':
                bot.send_message(user, 'В первую очередь вам необходимо '
                                       'зарегистрироваться или войти в уже существующий профиль.', reply_markup=menu)
                working, buyer = False, False
                is_fio, is_number, is_email, inf_about, number, fio, email = False, False, False, False, '', '', ''
                filtering, sorting, reverse_sorting, vpered, nazad, owner_data, zapros, nomer_poiska = False, False, False, False, False, [], [], 0
                is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor = False, False, False, False, False, False, False, False
                city, street, house, metro, rooms, price, area, floor = '', '', '', 0, 0, 0, 0, 0


            if filtering:
                if sms == 'Меню':
                    bot.send_message(user, 'Выберите действие', reply_markup=b_menu)
                    filtering, information, activity, searching = False, False, False, False
                    is_city, is_street, is_house, is_metro, is_rooms, is_price, is_area, is_floor = False, False, False, False, False, False, False, False
                    city, street, house, metro, rooms, price, area, floor = '', '', '', 0, 0, 0, 0, 0

                # elif is_street:
                #     street = sms
                #     is_street, is_house = False, True
                #     bot.send_message(user, 'Введите дом')
                # elif is_house:
                #     house = sms
                #     is_house, is_metro = False, True
                #     bot.send_message(user, 'Введите примерное расстояние от квартиры до метро (в метрах)')
                elif is_metro:
                    metro = sms
                    is_metro, is_rooms = False, True
                    bot.send_message(user, 'Введите количество комнат в квартире')
                elif is_rooms:
                    rooms = sms
                    is_rooms, is_price = False, True
                    bot.send_message(user, 'Введите цену за квартиру (в рублях)')
                elif is_price:
                    price = sms
                    is_price, is_area = False, True
                    bot.send_message(user, 'Введите площадь квартиры (в квадратных метрах)')
                elif is_area:
                    area = sms
                    is_area, sorting = False, True
                    bot.send_message(user, "Выберите действие: ", reply_markup=inmarkup)

                elif sorting:
                    vpered = True
                    is_zapros = True
                    owner_data = cursor.execute(f'SELECT * FROM owners').fetchall()

                    if is_zapros:
                        if sms == 'Вперед':
                            vpered = True

                        elif sms == 'Назад':
                            nazad = True

                        elif sms == 'Меню':
                            bot.send_message(user, "Выберите действие", reply_markup=b_menu)
                            vpered, nazad = False, False
                            nomer_poiska = 0
                            filtering, is_zapros, city, street, house, metro, rooms, price, area, floor, domoy = False, False, '', '', '', 0, 0, 0, 0, 0, False

                        if vpered:
                            if len(zapros) == 0:
                                bot.send_message(user, "Нет квартир с данными параметрами", reply_markup=b_menu)
                                vpered, nazad = False, False
                                nomer_poiska = 0
                                filtering, is_zapros, city, street, house, metro, rooms, price, area, floor, domoy = False, False, '', '', '', 0, 0, 0, 0, 0, False
                            else:
                                bot.send_message(user, f'Квартира по адресу: {zapros[nomer_poiska][2]}, '
                                                       f'{zapros[nomer_poiska][3]}, {zapros[nomer_poiska][4]} '
                                                   f'\nНаходится на {zapros[nomer_poiska][9]} этаже в {zapros[nomer_poiska][5]} метрах от'
                                                   f' ближайшего метро \nКоличество комнат: {zapros[nomer_poiska][6]} '
                                                   f'\nПлощадь (в квадратных метрах): {zapros[nomer_poiska][8]} '
                                                   f'\nЦена (в рублях): {zapros[nomer_poiska][7]}\n'
                                                   f'Владелец: ' + str(owner_data[nomer_poiska][1] if len(owner_data[nomer_poiska][1]) != 0 else "Не указан")
                                                 + "\nКонтактный номер: " + str(owner_data[nomer_poiska][2] if len(owner_data[nomer_poiska][2]) != 0 else "Не указан")
                                                 + "\nПочта владельца: " + str(owner_data[nomer_poiska][3] if len(owner_data[nomer_poiska][3]) != 0 else "Не указан"), reply_markup=poisk)
                                vpered = False
                            nomer_poiska += 1

                        elif nazad:
                            nomer_poiska -= 1
                            bot.send_message(user, f'Квартира по адресу: {zapros[nomer_poiska][2]}, '
                                                   f'{zapros[nomer_poiska][3]}, {zapros[nomer_poiska][4]} '
                                               f'\nНаходится на {zapros[nomer_poiska][9]} этаже в {zapros[nomer_poiska][5]} метрах от'
                                               f' ближайшего метро \nКоличество комнат: {zapros[nomer_poiska][6]} '
                                               f'\nПлощадь (в квадратных метрах):{zapros[nomer_poiska][8]} '
                                               f'\nЦена (в рублях): {zapros[nomer_poiska][7]}\n'
                                               f'Владелец: ' + str(owner_data[nomer_poiska][1] if len(owner_data[nomer_poiska][1]) != 0 else "Не указан")
                                               + "\nКонтактный номер: " + str(owner_data[nomer_poiska][2] if len(owner_data[nomer_poiska][2]) != 0 else "Не указан")
                                               + "\nПочта владельца: " + str(owner_data[nomer_poiska][3] if len(owner_data[nomer_poiska][3]) != 0 else "Не указан"), reply_markup=poisk)
                            nazad = False

            elif inf_about:
                if sms == 'Назад':
                    bot.send_message(user, 'Выберите действие', reply_markup=b_menu)
                    is_fio, is_number, is_email, inf_about = False, False, False, False
                elif is_fio:
                    fio = sms
                    bot.send_message(user, 'Введите свой номер')
                    is_fio, is_number = False, True

                elif is_number:
                    number = sms
                    bot.send_message(user, 'Введите свою почту')
                    is_number, is_email = False, True

                elif is_email:
                    email = sms
                    cursor.execute(f'UPDATE buyers SET b_fio = "{fio}", b_number = "{number}", b_email = "{email}" WHERE b_login = "{login}"')
                    bot.send_message(user, 'Информация успешно добавлена', reply_markup=b_menu)
                    is_email, inf_about = False, False

            elif sms == 'Посмотреть варианты квартир':
                filtering = True
                bot.send_message(user, 'Начинаем подбор:', reply_markup=back_)
                bot.send_message(user, 'Введите город', reply_markup=gorod)

            elif sms == 'Добавить информацию о себе':
                bot.send_message(user, 'Введите свое ФИО', reply_markup=back)
                inf_about, is_fio = True, True

            else:
                bot.send_message(user,'Выберите действие')


    elif sms == 'Зарегистрироваться':
        bot.send_message(user, 'Выберите сторону договора', reply_markup=reg)
        registration, reg_log = True, True


    elif sms == "Войти":
        bot.send_message(user, 'Введите логин', reply_markup=back)
        authorization, auth_passw = True, True


    else:
        bot.send_message(user, "Выберите существующее действие в меню", reply_markup=menu)


    connection.commit()
    connection.close()


bot.polling(none_stop=True)
