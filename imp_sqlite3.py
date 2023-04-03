'''
        Программа импорта данных из базы данных sqlite в файл CSV

        Конвертация данных из базы данных SQLite в файл CSV в Python может быть выполнена с помощью
        использования библиотеки sqlite3 и модуля csv. Вот пример программы на Python, которая извлекает
        данные из таблицы SQLite и сохраняет их в файл CSV:

        Замените mydatabase.db на имя вашей базы данных SQLite и mytable на имя таблицы, из которой вы
        хотите извлечь данные. Затем запустите программу, чтобы создать файл data.csv, содержащий данные
        из таблицы в базе данных SQLite.

'''
import sqlite3
import csv

# Установите соединение с базой данных SQLite
conn = sqlite3.connect('mydatabase.db')

# Получите курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Выполните SQL-запрос для получения данных из таблицы
cursor.execute('SELECT * FROM mytable')

# Получите данные из курсора
data = cursor.fetchall()

# Откройте файл CSV для записи
with open('data.csv', 'w', newline='') as csvfile:
    # Создайте объект writer для записи в файл CSV
    csvwriter = csv.writer(csvfile)

    # Запишите заголовки столбцов в файл CSV
    csvwriter.writerow([description[0] for description in cursor.description])

    # Запишите данные из таблицы в файл CSV
    for row in data:
        csvwriter.writerow(row)

# Закройте соединение с базой данных
conn.close()
