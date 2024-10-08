class Vehicle():
  def __init__(self, brand, model, year):
    self.__brand = brand
    self.__model = model
    self.__year = year
    self.__speed = 0
    self.__fuel = 100

  def start(self):
    self.__speed = 0
    self.__fuel -= 10
    return f"The {self.__brand} {self.__model} {self.__year} has started. The fuel is {self.__fuel}."

  def accelerate(self, spd, fl):
    if self.__speed > 1500:
      self.__speed = 1500
      return f"no"
    else:
      self.__speed += spd
      self.__fuel -= fl
      return f"The {self.__brand} {self.__model} {self.__year} is accelerating. The speed is now {self.__speed} and the fuel has decreased to {self.__fuel}."

  def honk(self, honk):
    return f"Insert honking sfx:{honk}"
   
  def geteverything(self):
    return f"{self.__brand} {self.__model} {self.__year}, speed is {self.__speed}, fuel is {self.__fuel}"
  def get_brand(self):
    return self.__brand
  def get_model(self):
    return self.__model
  def get_year(self):
    return self.__year
  def get_speed(self):
    return self.__speed
  def get_fuel(self):
    return self.__fuel
  def set_speed(self, spd):
    self.__speed = spd
  def set_fuel(self, fl):  
    if fl < 0:
      self.__fuel = 0
    elif fl > 100:
      self.__fuel = 100
    else:
      self.__fuel = fl

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

class Car(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.__enginepow = 10
    self.__honksfx = "Vroom"
    self.__spdinc = 10
    self.__fldc = 10
  def accelerate(self):
    return f"{super().accelerate(self.__spdinc, self.__fldc)}"
  def honk(self):
    return f"{super().honk(self.__honksfx)}"

class Truck(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.__enginepow = 5
    self.__honksfx = "Woof"
    self.__spdinc = 10
    self.__fldc = 15
  def accelerate(self):
    return f"{super().accelerate(self.__spdinc, self.__fldc)}"
  def honk(self):
    return f"{super().honk(self.__honksfx)}"

class Motorcycle(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.__enginepow = 15
    self.__honksfx = "Meow"
    self.__spdinc = 15
    self.__fldc = 5
  def accelerate(self):
    return f"{super().accelerate(self.__spdinc, self.__fldc)}"
  def honk(self):
    return f"{super().honk(self.__honksfx)}"
  
sedan = Car("Honda", "Civic", 2023)
truck = Truck("Ford", "F-150", 2023)
bike = Motorcycle("Yamaha", "MT-07", 2024)

print(sedan.geteverything())
print(truck.geteverything())
print(bike.geteverything())
sedan.set_speed(50)
print(sedan.geteverything())
sedan.set_speed(0)

print(sedan.start())
print(sedan.accelerate())
print(sedan.brake())
print(truck.start())
print(truck.accelerate())
print(truck.brake())
print(bike.start())
print(bike.accelerate())
print(bike.brake())

print(sedan.honk())
print(truck.honk())
print(bike.honk())