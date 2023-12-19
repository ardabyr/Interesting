import sqlite3 as sql
from faker import Faker
# import faker
from random import choice, randint

fake = Faker("ru_RU")
quantity = int(5e4)


logins = [fake.unique.user_name() for i in range(quantity)]
passwords = [fake.password(special_chars=False) for j in range(quantity)]
buy_owns = [fake.boolean() for k in range(quantity)]
numbers = [fake.unique.phone_number() for m in range(quantity)]
emails = [fake.unique.ascii_free_email() for n in range(quantity)]

connection = sql.connect(
            r'C:\Users\liubo\OneDrive\Документы\Skillbox_SQLite_Webinar-master\SQLiteStudio\bd_agency')
cursor = connection.cursor()


for t in range(len(logins)):
    cursor.execute(f'INSERT INTO people (login, password, buy_own) '
                   f'VALUES ("{logins[t]}", "{passwords[t]}", {buy_owns[t]})')

    if buy_owns[t]:
        cursor.execute(f'INSERT INTO owners (o_login, o_fio, o_number, o_email) '
                       f'VALUES ("{logins[t]}", "{fake.name()}", "{numbers[t]}", "{emails[t]}")')
    else:
        cursor.execute(f'INSERT INTO buyers (b_login, b_fio, b_number, b_email) '
                       f'VALUES ("{logins[t]}", "{fake.name()}", "{numbers[t]}", "{emails[t]}")')

connection.commit()
connection.close()

##############################################################################################

connection = sql.connect(
            r'C:\Users\liubo\OneDrive\Документы\Skillbox_SQLite_Webinar-master\SQLiteStudio\bd_agency')
cursor = connection.cursor()

logins = [sim[0] for sim in cursor.execute(f'SELECT login FROM people').fetchall()]
city = ["Москва", "Санкт-Петербург", "Нижний Новгород", "Новосибирск", "Казань"]

for i in range(quantity):
    rand = randint(1, 3)
    if rand == 1:
        pass
    else:
        cursor.execute(f'INSERT INTO apts (o_login, a_city, a_street, a_house, a_metro, a_rooms, a_price, '
                       f'a_area, a_floor) VALUES ("{choice(logins)}", "{choice(city)}", '
                       f'"{fake.street_name()}", "{fake.building_number()}", '
                       f'"{randint(1, 50) * 100}", "{randint(1,7)}", "{randint(5, 150) * 1e5}", '
                       f'"{randint(20, 300)}", "{randint(1, 100)}")')


connection.commit()
connection.close()
