'''
        Программа импорта данных из базы данных postgresql в файл CSV

        Пример программы на Python, которая экспортирует данные из таблицы PostgreSQL в файл CSV:

        В этом примере мы используем библиотеку psycopg2 для подключения к базе данных PostgreSQL
        и выполнения запросов к ней. Затем мы выполняем запрос на выборку данных из таблицы mytable,
        получаем данные из курсора и записываем их в файл CSV с помощью стандартной библиотеки csv.

        ** Обратите внимание, что перед записью данных в файл CSV мы записываем заголовки столбцов с помощью
           свойства description объекта курсора. Вы можете изменить запрос на выборку данных, чтобы выбирать
           только те столбцы и строки, которые вам нужны. Также вы можете настроить параметры подключения к
           базе данных, чтобы соответствовать вашей конфигурации.

'''
import psycopg2
import csv

# Параметры подключения к базе данных
db_host = "localhost"
db_name = "mydatabase"
db_user = "myuser"
db_password = "mypassword"

# Подключение к базе данных
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

# Открытие курсора для выполнения запросов
cur = conn.cursor()

# Выполнение запроса на получение данных
cur.execute("SELECT * FROM mytable")

# Получение данных из курсора
rows = cur.fetchall()

# Закрытие курсора и соединения с базой данных
cur.close()
conn.close()

# Запись данных в файл CSV
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cur.description])
    for row in rows:
        writer.writerow(row)
