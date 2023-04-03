'''
    Пример программы на Python для импорта данных из CLI в базу данных SQLite:

    В этом примере программа создает базу данных SQLite с именем "mydatabase.db" и таблицу "users",
    если они еще не существуют. Затем программа запрашивает данные у пользователя в CLI и добавляет
    их в таблицу с помощью запроса INSERT INTO. Наконец, программа закрывает соединение с базой данных.

    Обратите внимание, что этот код подвержен SQL-инъекциям, поэтому настоятельно рекомендуется
    использовать параметризованные запросы для защиты от таких атак.

'''

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER)''')

# Пользовательский ввод данных в CLI
name = input('Введите имя пользователя: ')
age = int(input('Введите возраст пользователя: '))

# Добавление данных в таблицу
cursor.execute(f"INSERT INTO users (name, age) VALUES ('{name}', {age})")
conn.commit()

# Закрытие соединения с базой данных
conn.close()
