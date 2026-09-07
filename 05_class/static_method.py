class Fruit:
  def __init__(self,name,color):
    self.name = name
    self.color = color

  @staticmethod
  def class_type():
    return "Fruit"

my_fruit = Fruit("Mango","Yellow")

print(my_fruit.class_type())

print(Fruit.class_type())