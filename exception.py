# Обробка винятків. Конструкція "try - except"
# num = None

# while num == None:
#   try:
#     num = int(input("Enter a number: "))
#     num += 5
#     print(num)
#   except ValueError:
#     print("You entered not a number")

try: 
  a = 10
  b = int(input("Enter a number: "))
  print(a / b)
except ValueError:
  print("You entered not a number")
except ZeroDivisionError:
  print("You entered zero")
# Застосовується до всіх видів помилок, але не вказується конкретно яка помилка сталася  
# except Exception:
#   print("Unknown error")
else:
  print("You are a genious!")
# finally:
#   print("Anyway well done")



