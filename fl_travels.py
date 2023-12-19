import pandas as pd
import matplotlib.pyplot as plt

# Считываем файлы в переменные, не забыв указать разделитель sep

travels = pd.read_csv("travels.csv", sep=';')
travel_agents = pd.read_csv("travel_agents.csv", sep=';')
sale_of_tour_packages = pd.read_csv("sale_of_tour_packages.csv", sep=';')

# 1.	Найти количество человек, совершивших путешествие в региональные центры.

# Выберем из таблицы sale_of_tour_packages столбик с количеством проданных путевок

people = sale_of_tour_packages["Количество проданных путёвок"]
# Проссумируем все значения и выведем на экран
print("Количество человек, совершивших путешествие в региональные центры:", people.sum())

# 2.	Построить круговую диаграмму, отображающую общую стоимость путевок и стоимость
#           путевок по каждому городу, которые были проданы туроператором "Горизонт".

# Объединим данные о продажах с информацией о турах и туроператорах
merged_sales_df = sale_of_tour_packages.merge(travels, on='ID тура').merge(travel_agents, on='ID туроператора')

# Выберем данные только для туроператора "Горизонт"
gorizont_sales_df = merged_sales_df[merged_sales_df['Название'] == 'Горизонт']

# Суммируем стоимость путевок по каждому городу
city_total_cost = gorizont_sales_df.groupby('Город')['Стоимость, на 1 чел'].sum()

# Создаем круговую диаграмму
plt.figure(figsize=(10, 6))
plt.pie(city_total_cost, labels=city_total_cost.index, autopct='%1.1f%%')
plt.title('Общая стоимость путевок по каждому городу')
plt.show()

# 3.	Построить диаграмму, показывающую количество проданных путевок туроператором "Мечта" в каждый из дней.

# Выберем данные только для туроператора "Мечта"
mechta_sales_df = merged_sales_df[merged_sales_df['Название'] == 'Мечта']

# Сгруппируем данные по дате и посчитаем количество проданных путевок в каждый из дней
daily_sales = mechta_sales_df.groupby('Дата')['Количество проданных путёвок'].sum()

# Построим график
daily_sales.plot(kind='bar', figsize=(12, 8), title='Количество проданных путевок туроператором "Мечта" в каждый из дней')
plt.xlabel('Дата')
plt.ylabel('Количество проданных путёвок')
plt.show()
