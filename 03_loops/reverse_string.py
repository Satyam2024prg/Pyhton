string = input("Enter the string you want to reverse : ")
rev_str = ""

for char in string:
  rev_str = char + rev_str

print(f"Reversed string is {rev_str}")