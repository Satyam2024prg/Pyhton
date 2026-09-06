class Car:
  def __init__(self,brand,color):
    self.__brand = brand
    self.color = color

  def get_brand(self):
    return self.__brand


myCar = Car("Toyota","Black")

# print(myCar.__brand)  # not accessible
print(myCar.get_brand())
print(myCar.color)
