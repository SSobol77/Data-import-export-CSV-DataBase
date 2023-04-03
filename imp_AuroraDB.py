'''
        Программа импорта данных из базы данных Aurora DB в файл CSV.

        Для импорта данных из базы данных Aurora DB в файл CSV с помощью Python необходимо выполнить следующие шаги:

        ** Обратите внимание, что в данном примере мы использовали DictWriter для записи данных в CSV файл, так как
           данные в Aurora DB были получены в виде списка словарей. Если вы используете другой способ получения данных,
           то можете использовать другой подход для записи данных в файл.

        ШАГИ:

        1. Установить библиотеку boto3 для работы с AWS SDK:
                                                            pip install boto3
'''

# 2. ----    Создать соединение с базой данных Aurora DB:  --------------------------------------------

import boto3

# Указываем параметры для подключения к базе данных Aurora DB
host = '<aurora_db_cluster_endpoint>'
port = 3306
database = '<database_name>'
user = '<user_name>'
password = '<password>'

# Создаем соединение с базой данных
client = boto3.client('rds-data')

response = client.execute_statement(
    secretArn='<secret_arn>',
    database=database,
    resourceArn='<resource_arn>',
    sql=f"SELECT * FROM <table_name>"
)

# Получаем данные из ответа в виде списка словарей
data = response['records']

# 3. Преобразовать данные в формат CSV и записать в файл:
import csv

# Определяем названия столбцов в CSV файле
fieldnames = ['column1', 'column2', 'column3']

with open('data.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Записываем данные в CSV файл
    for row in data:
        writer.writerow({
            'column1': row[0]['stringValue'],
            'column2': row[1]['stringValue'],
            'column3': row[2]['longValue'],
        })
