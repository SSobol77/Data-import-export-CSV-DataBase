'''
    Пример программы на Python для импорта данных из CLI в базу данных MySQL:

    - Обратите внимание, что для работы программы необходимо иметь установленный
      и запущенный сервер базы данных MySQL.
    - Также требуется установить библиотеку Python mysql-connector-python.
'''

import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Получение курсора
mycursor = mydb.cursor()

# Запрос на вставку данных в таблицу
sql = "INSERT INTO yourtable (column1, column2, column3) VALUES (%s, %s, %s)"

# Ввод данных из командной строки
val1 = input("Введите значение для column1: ")
val2 = input("Введите значение для column2: ")
val3 = input("Введите значение для column3: ")

# Значения для вставки в таблицу
values = (val1, val2, val3)

# Выполнение запроса на вставку данных
mycursor.execute(sql, values)

# Подтверждение изменений в базе данных
mydb.commit()

# Вывод количества вставленных записей
print(mycursor.rowcount, "запись добавлена в таблицу")
