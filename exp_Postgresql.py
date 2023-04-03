'''
    Пример программы на Python для импорта данных из CLI в базу данных PostgreSQL:

    Для запуска этой программы вам понадобится установить библиотеку psycopg2, например, с помощью pip:
        \> pip install psycopg2

    Также перед запуском программы необходимо заменить значения host, database, user и password на свои
    настройки соединения с базой данных PostgreSQL.

'''

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# Создание курсора
cur = conn.cursor()

# Запрос имени таблицы, в которую будут импортироваться данные
table_name = input("Введите имя таблицы: ")

# Запрос количества столбцов таблицы
num_cols = int(input("Введите количество столбцов: "))

# Создание списка столбцов таблицы
cols = []
for i in range(num_cols):
    col_name = input("Введите имя столбца: ")
    cols.append(col_name)

# Запрос данных для импорта
print("Введите данные для импорта:")
while True:
    try:
        values_str = input().strip()
        if not values_str:
            break
        values = values_str.split()
        if len(values) != num_cols:
            raise ValueError
        # Формирование запроса на вставку данных
        query = f"INSERT INTO {table_name} ({','.join(cols)}) VALUES ({','.join(['%s']*num_cols)})"
        cur.execute(query, values)
    except ValueError:
        print("Некорректное количество значений")
    except Exception as e:
        print(f"Ошибка вставки данных: {e}")
        break

# Фиксация изменений в базе данных
conn.commit()

# Закрытие курсора и соединения
cur.close()
conn.close()


