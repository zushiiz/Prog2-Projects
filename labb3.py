class Vehicle():
  def __init__(self, brand, model, year):
    self.__brand = brand
    self.__model = model
    self.__year = year
    self.__speed = 0
    self.__fuel = 100

  def start(self):
    self.__fuel -= 10
    return f"The {self.__brand} {self.__model} {self.__year} has started. The fuel is {self.__fuel}."

  def accelerate(self):
    self.__speed += self.enginepow
    self.__fuel -= 10
    return f"The {self.__brand} {self.__model} {self.__year} is accelerating. The speed is now {self.__speed} and the fuel has decreased to {self.__fuel}."  

  def brake(self):
    self.__speed -= 10
    return f"The {self.__brand} {self.__model} {self.__year} is braking. The speed is now {self.__speed}."  
  
  def setspeed(self, s):
    if s < 0:
      self.__speed = 0
    else:
      self.__speed = s

  def refuel(self):
    self.__fuel = 100
    return f"The {self.__brand} {self.__model} {self.__year} has been refueled. The fuel is now {self.__fuel}."
  
  def setfuel(self, f):
    if f < 0:
      self.__fuel = 0
    elif f > 100:
      self.__fuel = 100
    else:
      self.__fuel = f

  def honk(self):
    return f"Insert honking sfx:{self.honksfx}"  
  
  def getspeedfuel(self):
    return self.__fuel, self.__speed

class Car(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.enginepow = 10
    self.honksfx = "Quack"

class Truck(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.enginepow = 5
    self.honksfx = "Woof"

class Motorcycle(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.enginepow = 15
    self.honksfx = "Meow"

sedan = Car("Honda", "Civic", 2023)
truck = Truck("Ford", "F-150", 2023)
bike = Motorcycle("Yamaha", "MT-07", 2024)

print(sedan.start())
print(sedan.accelerate())
print(sedan.brake())
print(sedan.refuel())
print(sedan.honk())

print(truck.start())
print(truck.accelerate())
print(truck.honk())

print(bike.getspeedfuel())
bike.setspeed(50)
bike.setfuel(10)
print(bike.getspeedfuel())