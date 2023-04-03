'''

    Пример программы на Python для импорта данных из CLI в базу данных MongoDB, используя модуль pymongo:

    В этом примере мы подключаемся к базе данных MongoDB на локальном хосте, создаем базу данных "mydatabase"
    и коллекцию "mycollection". Затем запрашиваем данные от пользователя в CLI с помощью функции input(), и
    добавляем их в коллекцию MongoDB с помощью метода insert_one(). Наконец, мы закрываем соединение с базой данных.

'''

import pymongo

# Подключение к базе данных
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Запрос данных из CLI
data = input("Введите данные для импорта в базу данных: ")

# Добавление данных в коллекцию MongoDB
collection.insert_one({"data": data})

# Закрытие соединения с базой данных
client.close()
