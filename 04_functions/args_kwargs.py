def sum(*args):
  add = 0
  for i in args:
    add += i
  return add

def prod(**kwargs):
  return kwargs


print(sum(5,5))
print(sum(5,5,5))
print(sum(5,5,5,5))

print(prod(a=2,b=10))
print(prod(a=2,b=10,c=5))