class Car():
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.speed = 0

  def start(self):
    print(f"{self.brand} {self.model} {self.year} has started. The current speed is {self.speed}")
  
  def stop(self):
    self.speed = 0
    print(f"{self.brand} {self.model} {self.year} has stopped. The current speed is {self.speed}")    

  def accelerate(self, increase):
    self.speed += increase
    print(f"{self.brand} {self.model} {self.year} has accelerated. The current speed is {self.speed}")

  def brake(self, decrease):
    self.speed -= decrease
    print(f"{self.brand} {self.model} {self.year} has decelerated. The current speed is {self.speed}")

class Electriccar(Car):
  def __init__(self, brand, model, year, battery):
    super().__init__(brand, model, year)
    self.battery = battery
  
  def charge(self):
    print(f"{self.brand} {self.model} {self.year} has charged. The battery is currently {self.battery}kWh")
  
class Sportscar(Car):
    def __init__(self, brand, model, year, turbo):
      super().__init__(brand, model, year)
      self.turbo = turbo
    
    def activateturbo(self):
      if self.turbo == True:
        self.speed += 50
        print(f"{self.brand} {self.model} {self.year} has activated turbo. The current speed is {self.speed}")
      else:
        print(f"{self.brand} {self.model} {self.year} does not have turbo")
        
tesla = Electriccar("Tesla", "Model_S", "2021", 100)
ferrari = Sportscar("Ferrari", "488", "2022", True)

tesla.start()
tesla.accelerate(60)
tesla.charge()
tesla.brake(30)
tesla.stop()

ferrari.start()
ferrari.accelerate(100)
ferrari.activateturbo()
ferrari.brake(120)
ferrari.stop()