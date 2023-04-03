'''

        Пример программы импорта данных  из CLI в базу данных IBM DB2:

        Для импорта данных из CSV файла в базу данных DB2 можно использовать следующий пример программы на языке Python:

        * Необходимо заменить значения в функции ibm_db.connect() на свои значения, соответствующие подключению к базе
          данных DB2. Также нужно указать имя таблицы и столбцов в запросе на вставку данных.
'''
import ibm_db
import csv

# подключение к базе данных
conn = ibm_db.connect("DATABASE=mydb;HOSTNAME=myserver;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypass", "", "")

# открытие CSV файла и чтение данных
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # пропускаем заголовок
    for row in reader:
        # вставка данных в таблицу
        query = f"INSERT INTO mytable (column1, column2, column3) VALUES ({row[0]}, {row[1]}, {row[2]})"
        stmt = ibm_db.exec_immediate(conn, query)

# закрытие соединения
ibm_db.close(conn)
