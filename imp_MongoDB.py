'''
        Программа импорта данных из базы данных MongoDB в файл CSV
        @SSobol77

        Для импорта данных из базы данных MongoDB в файл CSV можно использовать следующий код на Python
        с помощью библиотеки pymongo:

        ** В данном примере мы подключаемся к базе данных MongoDB, получаем коллекцию и извлекаем данные из
        нее с помощью метода find(). Затем мы открываем файл data.csv в режиме записи и записываем заголовки
        столбцов и данные из коллекции в формате CSV с помощью модуля csv.
'''
import csv
import pymongo

# Подключение к базе данных MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Получение коллекции
collection = db['mycollection']

# Получение данных из коллекции
cursor = collection.find()

# Запись данных в файл CSV
with open('data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'gender']) # Запись заголовков столбцов
    for document in cursor:
        writer.writerow([document['name'], document['age'], document['gender']])
