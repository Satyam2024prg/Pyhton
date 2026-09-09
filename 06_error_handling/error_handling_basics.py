file = open('text.txt','w')

try:
  file.write('Hello World')
finally:
  file.close()

with open('text2.txt','w') as file:
  file.write('Text2 file')