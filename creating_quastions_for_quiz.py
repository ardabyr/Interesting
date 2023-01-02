import sqlite3  #

db = sqlite3.connect('quastions.db')  # создаем или заходим в уже созданную БД
cur = db.cursor()  # создаем функцию курсора для управления БД

cur.execute("""CREATE TABLE IF NOT EXISTS quast(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   quastion TEXT,
   answ_1 TEXT,
   answ_2 TEXT,
   answ_3 TEXT,
   right_answ INT
   )""")  # загружаем поля в БД, если она не была создана раньше
db.commit()  # подтверждаем действие


def vvod():
    qus, a1, a2, a3, ra = input("Your quastion: "), input("First answer: "), input("Second answer: "), \
                          input("Third answer: "), input("Right answer: ")
    # переменные для вопросов и ответов
    cur.execute("""
    INSERT INTO quast(quastion, answ_1, answ_2, answ_3, right_answ)
     VALUES (?, ?, ?, ?, ?);""", (qus, a1, a2, a3, ra))  # загружаем данные в таблицу

    db.commit()  # подтверждаем действие


def show():
    s = cur.execute("SELECT * FROM quast ")  # запрашиваем данные всей таблицы
    for sim in s:
        print(sim)  # печатаем их


while True:
    do = int(input("""Введите 1, если хотите посмотреть данные,
Введите 2, елси хотите добавить вопрос,
Введите 3, если хотите выйти из программы\n"""))
    if do == 1:
        show()
    elif do == 2:
        vvod()
    elif do == 3:
        break
    # в цикле можем добавлять данные и смотреть на них




