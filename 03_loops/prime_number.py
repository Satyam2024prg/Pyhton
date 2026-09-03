num = int(input("Enter a number : "))

flag = 0

if num < 0:
  flag = 1
  print("Negative numbers are not prime")
elif num == 0 or num == 1:
  flag = 1
  print(f"{num} is not a prime number")
else :
  for i in range(2,num):
    if num % i == 0:
      print(f"{num} is not prime number")
      flag = 1
      break

if flag == 0:
  print(f"{num} is prime number")