# Спадкування, поліморфізм, інкапсуляція

# class Build:
#   # Робимо властивість приватною додавши два нижніх підкреслення
#   __year = None
#   __city = None
  
#   def __init__(self, year, city):
#     self.year = year
#     self.city = city
    
#     # self.get_info()
    
#   def get_info(self):
#     print("Year: ", self.year, ". City: ", self.city, sep="")
    
    
# class School(Build):
#   __pupils = None
  
#   def __init__(self, year, city, pupils=500):
#     super(School, self).__init__(year, city)
#     self.pupils = pupils
    
#   def get_info(self):
#         super().get_info()  
#         print("Pupils: ", self.pupils)

# class House(Build):
#   __appartments = None
  
#   def __init__(self, year, city, appartments=5):
#     super(House, self).__init__(year, city)
#     self.appartments = appartments
    
#   def get_info(self):
#         super().get_info()  
#         print("Appartments: ", self.appartments)

# class Shop(Build):
#   pass


# school = School(1990, "Seattle", 700)
# school.get_info()

# house = House(2010, "New York", 7)
# house.get_info()

# shop = Shop(2000, "Los Angeles")
