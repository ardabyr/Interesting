from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # метод для отображения фигуры в окне
import matplotlib.pyplot as plt


class Degrees:
    def __init__(self):
        self.root = Tk()  # создаем окно программы
        self.root.title('file diagram')  # создаем заголовок программы
        self.root.geometry("500x500")  # создаем размеры окна
        self.root.resizable(False, False)
        Label(self.root, text="File:").pack()  # Создаем текстовые надписи
        self.lb1 = Label(self.root, text="---")  # Добавим место для названия файла
        self.lb1.pack()  # отрисуем на экране
        self.btn = ttk.Button(text='choose', command=self.open)  # создаем кнопку для открытия файла,
        # которая использует функцию, которую напишем далее
        self.btn.pack()  # визуализируем кнопку
        self.file = None  # создаем изначально пустую переменную для хранения файла
        Button(self.root, text='show', command=self.show).pack()  # создаем вторую внопку для отрисовки диаграммы

        matplotlib.use('Tkagg')  # это связь tkinter и matpotlib

        self.root.mainloop()  # зацикливаем все действия, чтобы окно не пропало сразу же после создания

    def open(self):  # создаем функцию для открытия проводника и дальнейшего выбора файла
        file_name = fd.askopenfilename()  # запоминаем название файла (путь к файлу)
        fk = open(file_name, encoding="utf-8")  # открываем файл, используя utf-8
        self.file = fk.readlines()  # сохраняем все в зарезервированную переменную,
        # сразу считывая данные в список из строк
        self.lb1["text"] = file_name  # в переменную для названия файла запишем наше название

    def show(self):  # создаем функцию для отрисовки диаграммы
        name, price = [], []  # списки для обработки данных файла
        for i in range(len(self.file)):  # в цикле в первый список добавляем поочередно все названия товаров
            # а во второй список цифру, которая состоит из произведения количества на цену
            predmet = self.file[i].split()
            name.append(predmet[0])
            price.append(int(predmet[1]) * int(predmet[2]))

        pie = plt.figure(figsize=(5, 5), facecolor=(1, 1, 1))  # задаем размер диаграммы и задний фон - белый
        pie.labels = name  # присваиваем наши названия, чтобы они отображались у нужных данных
        pie.sizes = price  # сами данные
        pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes,
                                                    labels=pie.labels,
                                                    autopct='% 3.1f %%',  # Значение сохраняет десятичные знаки
                                                    )  # собираем все наши предыдущие "настройки" в одну фигуру

        canvas = FigureCanvasTkAgg(pie, self.root)  # еще одно действие для связи нашей фигуры с tkinter
        canvas.get_tk_widget().pack()  # отображаем ее на экране


if __name__ == "__main__":
    Degrees()  # запускаем программу
