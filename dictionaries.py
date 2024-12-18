#Словники це типу об'єкти, при створенні словників ми використовуємо {}. Ключем може бути будь яке значення окрім спсиків.

# person = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(person)
# print(person['age'])
#Заміна ключа можна робити за назвою ключа або індексом
# person['age'] = 31
# print(person)

# pers = dict(name='John', age=30, city='New York') 
# print(pers)

# print(person.keys())
#Виводяться як ключі так і значення
# print(person.items())

# for key, values in person.items():
#   print(key, values, sep=" - ")
  
# for el in person.keys():
#   print(el)
# for el in person.values():
#   print(el)

# person = {'name': 'John', 'age': 30, 'city': 'New York'}
# # print(person.get("name"))
# # person.popitem()
# person["bio"] = "Hello"
# print(person)


# people = {
#   "user_1": {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "grades": {"math": 80, "english": 70, "history": 85}
#   },
#   "user_2": {
#     "name": "Jane",
#     "age": 25,
#     "city": "San Francisco",
#     "grades": {"math": 90, "english": 80, "history": 75}
#   }
# }

# print(people["user_1"]["grades"]["math"])
# print(people["user_2"]["city"])
# print(people)
