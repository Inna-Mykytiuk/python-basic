#Основи ООП. Створення класу та об'єкта
class Dog:
  name = None 
  age = None
  isHappy = None
  
  def set_data(self, name, age, isHappy):
    self.name = name
    self.age = age
    self.isHappy = isHappy
    
  def get_data(self):
    print(self.name, "Age:", self.age, "Is happy:", self.isHappy)
  
dog1 = Dog()
dog1.set_data("Scooby", 5, True)

dog2 = Dog()
dog2.set_data("Max", 3, False)

# print(dog1.name)
# print(dog2.name)

dog1.get_data()
dog2.get_data()