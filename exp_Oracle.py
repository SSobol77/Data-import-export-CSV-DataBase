'''
        Пример программы импорта данных  из CLI в базу данных Oracle:

        Для импорта данных из CLI в базу данных Oracle на Python нужно использовать
        библиотеку cx_Oracle. Ниже приведен пример кода для импорта данных из файла CSV в таблицу Oracle.

        Замените username, password, host, port и sid на соответствующие значения для вашей базы данных Oracle.
        Также замените data.csv на имя вашего файла с данными и table_name на имя таблицы, в которую вы хотите
        импортировать данные.

        Пример data.csv :
                name,age,city
                John,32,New York
                Jane,28,San Francisco
                Tom,45,Chicago
                Emily,22,Boston

        * Это простой файл CSV (Comma Separated Values), который содержит три поля:
          name, age и city. Каждая строка содержит данные для одной записи в таблице.
'''

import cx_Oracle
import csv

# Установка соединения с базой данных
conn = cx_Oracle.connect('username/password@host:port/sid')

# Открытие файла CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    # Итерация по строкам в CSV-файле
    for row in reader:
        # Вставка данных в таблицу
        cursor = conn.cursor()
        cursor.execute("INSERT INTO table_name (column1, column2, column3) VALUES (:1, :2, :3)", (row[0], row[1], row[2]))
        cursor.close()

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
