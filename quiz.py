from tkinter import *
from random import shuffle  # функция случайного выбора элемента из списка
import sqlite3


class Victorina:
    def __init__(self):
        self.root = Tk()  # создаем окно программы
        self.root.title('Викторина')  # создаем заголовок программы
        self.root.geometry("350x250")  # создаем размеры окна
        self.counter = 0  # создаем счетчик для правильных ответов
        self.var = IntVar()  # переменная для ожидания нажатия кнопки
        self.cor_ans = 0  # переменная верного ответа для данного вопроса
        self.p1, self.p2, self.p3 = '', '', ''  # номера вариантов ответов
        self.answ = ""  # перменная для правильного ответа
        self.q1, self.lb1, self.lb2, self.lb3 = Label(self.root, text="1"), Label(self.root, text="2"), \
                            Label(self.root, text="3"), Label(self.root, text="4")
        # создаем текстовые надписи для вопросоа и трех ответов, в последствии будем менять текст на них
        self.input = Entry(self.root)  # поле для ввода ответов
        self.btn_answ = Button(self.root, text="Ответить", command=self.skip)  # кнопка для ответа
        Label(self.root, text="\n").pack()  # небольшой отступ в окне
        self.btn = Button(self.root, text="Начать", command=self.start)  # кнопка для начала викторины
        self.btn.pack()  # отобраажаем кнопку запуска
        self.db = None  #
        self.cursor = None
        self.quast = None
        self.lenght = 0
        self.root.mainloop()  # зацикливаем

    def start(self):  # функция свмой викторины
        self.get_db()  # запускаем функцию по обработке БД
        self.btn.destroy()  # удаляем кнопку начала
        ib = [i for i in range(1, self.lenght + 1)]  # задаем список id
        shuffle(ib)  # перемещиваем id вопросов, по ним и будем выбирать вопросы
        for i in range(5):  # выбираем вопросы только 5 раз
            self.q1["text"] = list(self.cursor.execute(f"SELECT quastion FROM quast WHERE id IS {ib[i]}"))[0][0]
            # присваиваем текст для поля текста с вопросом
            self.lb1["text"] = "1) " + list(self.cursor.execute(f"SELECT answ_1 FROM quast WHERE id IS {ib[i]}"))[0][0]
            self.lb2["text"] = "2) " + list(self.cursor.execute(f"SELECT answ_2 FROM quast WHERE id IS {ib[i]}"))[0][0]
            self.lb3["text"] = "3) " + list(self.cursor.execute(f"SELECT answ_3 FROM quast WHERE id IS {ib[i]}"))[0][0]
            # задаем текст для полей ответов
            self.cor_ans = list(self.cursor.execute(f"SELECT right_answ FROM quast WHERE id IS {ib[i]}"))[0][0]
            # задаем верный ответ
            self.q1.pack(); self.lb1.pack(); self.lb2.pack(); self.lb3.pack()  # отображем новый текст на экране
            self.input.pack()  # отображаем поле ввода на экране
            self.btn_answ.pack()  # и кнопку перехода к следующему вопросу
            self.btn_answ.wait_variable(self.var)  # функция ожидания начажатия кнопки

        self.btn_answ.destroy(); self.q1.destroy(); self.lb1.destroy()  # после завершения викторины удаляем все
        self.lb2.destroy(); self.lb3.destroy(), self.input.destroy()  # оставшиеся кнопки
        Label(self.root, text=f"Ваш результат: {self.counter} из {self.lenght}").pack()  # создаем текстовое поле для отображения результата
        te = ''
        if 0 < int(self.counter) / self.lenght < 0.5:
            te = "Всегда есть, к чему стремиться"
        elif 0.5 <= int(self.counter) / self.lenght < 0.9:
            te = "Хорошо"
        elif int(self.counter) / self.lenght >= 0.9:
            te = "Замечательно!"
        # вычисляем результат
        Label(self.root, text=te+"\n").pack()  # отображаем его на экране
        Button(self.root, text="Выйти", command=self.root.destroy).pack()  # делаем кнопку выхода

    def skip(self):  # функция перехода от вопроса к вопросу
        self.var.set(1)  # задаем переменную для ожидания нажатия кнопки
        self.answ = self.input.get()  # получаем введенные данные
        if self.answ == str(self.cor_ans):
            self.counter += 1
        # вычисляем верность ответа и инкрементируем счетчик
        self.input.delete(0, END)  # удаляем ввод пользователя
        self.input.pack()  # отображаем новое поле ввода

    def get_db(self):
        self.db = sqlite3.connect('quastions.db')  # подключаемся к нашей БД
        self.cursor = self.db.cursor()  # создаем указатель для работы с БД
        self.quast = [sim[0] for sim in self.db.execute("SELECT quastion FROM quast")]  # собираем столбец вопросов из БД
        self.lenght = len(self.quast)  # задаем длину всех действий


if __name__ == "__main__":
    Victorina()  # запускаем программу
