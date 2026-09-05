class Car:
  def __init__(self,brand,color):
    self.brand = brand
    self.color = color

class ElectricCar(Car):
  def __init__(self,brand,color,batterySize):
    super().__init__(brand,color)
    self.batterySize = batterySize

  

myCar = ElectricCar("Toyota","Red","Medium")

print(myCar)
print(myCar.brand)
print(myCar.color)
print(myCar.batterySize)