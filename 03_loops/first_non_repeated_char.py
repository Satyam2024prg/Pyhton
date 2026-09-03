string = input("Enter String in which you want to find the first non repeated character : ")

for char in string:
  if string.count(char) == 1:
    print(f"First non repeated character is {char}")
    break