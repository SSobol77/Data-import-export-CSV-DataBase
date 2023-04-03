'''
        Импорта данных из базы данных DB2 в файл CSV
        Для работы с базой данных DB2 в Python нам нужно использовать драйвер DB2. Один из таких драйверов - ibm_db,
        который можно установить с помощью pip.

        Предположим, что у нас есть база данных DB2 с таблицей "employees", которая содержит информацию о сотрудниках.
        Мы хотим экспортировать данные из этой таблицы в файл CSV.

        Вот пример программы на Python, которая использует модуль ibm_db для подключения к базе данных DB2, извлекает
        данные из таблицы "employees" и записывает их в файл CSV:

        ** В этом примере мы сначала устанавливаем соединение с базой данных DB2, используя данные для подключения,
           указанные в переменных. Затем мы выполняем SQL-запрос для извлечения данных из таблицы "employees" и используем
           функцию fetch_assoc для получения результата запроса в виде списка словарей, где каждый словарь соответствует
           строке данных в таблице. Затем мы создаем файл CSV и записываем заголовки столбцов в первую строку файла, а
           затем итерируемся по списку строк и записываем значения в соответствующие столбцы. Наконец, мы закрываем соединение
           с базой данных.
'''
import ibm_db
import csv

# Подключение к базе данных DB2
dsn_driver = "{IBM DB2 ODBC Driver}"
dsn_database = "my_database"
dsn_hostname = "my_hostname"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "my_username"
dsn_pwd = "my_password"
dsn_security = "SSL"
dsn = (
    f"DRIVER={dsn_driver};"
    f"DATABASE={dsn_database};"
    f"HOSTNAME={dsn_hostname};"
    f"PORT={dsn_port};"
    f"PROTOCOL={dsn_protocol};"
    f"UID={dsn_uid};"
    f"PWD={dsn_pwd};"
    f"SECURITY={dsn_security};"
)
conn = ibm_db.connect(dsn, "", "")

# Извлечение данных из таблицы "employees"
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM employees")
rows = ibm_db.fetch_assoc(stmt)

# Запись данных в файл CSV
with open('employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(rows[0].keys())
    for row in rows:
        writer.writerow(row.values())

# Закрытие соединения с базой данных
ibm_db.close(conn)
