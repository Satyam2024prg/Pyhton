num = int(input("Enter the number upto which you want to get the sum of even numbers : "))

sum = 0

for i in range(num+1):
  if (num > 0 and i % 2 == 0):
    sum += i

print(f"Sum of even numbers upto {num} is {sum}")