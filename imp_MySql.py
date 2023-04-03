'''
        Программа импорта данных из базы данных MySql в файл CSV
        @SSobol77

        Пример программы на Python, которая осуществляет импорт данных из базы данных MySQL в файл CSV:

        ** В этом примере мы используем модуль mysql.connector для подключения к базе данных MySQL и
           получения данных из таблицы. Затем мы записываем данные в файл CSV, используя модуль csv.
           Обратите внимание, что вам нужно заменить host, user, password, database, mytable на свои
           значения в соответствии с вашей базой данных MySQL.

'''
import mysql.connector
import csv

# Подключаемся к базе данных MySQL
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

# Получаем данные из таблицы
cursor = db.cursor()
cursor.execute("SELECT * FROM mytable")
data = cursor.fetchall()

# Записываем данные в CSV-файл
with open('data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])
    for row in data:
        writer.writerow(row)

# Закрываем соединение с базой данных
db.close()
