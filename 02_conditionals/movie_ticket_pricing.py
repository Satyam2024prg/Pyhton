day = input("Enter day : ")
age = int(input("Enter your age : "))

price = 0

if age < 18:
  price = 8
elif age >= 18:
  price = 12


if day.lower() == "wednesday":
  price = price - 2

print(price)