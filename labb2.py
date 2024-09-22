class Pokemon():                     # Defines a class
  def __init__(self, name, lvl):     # Constructor to set up values for the Class
    self.name = name                 # Attributes for the Class
    self.lvl = lvl
    self.hp = 100
  
  def stats(self):                   # Method called stats() in the Class
    return f"{self.name} is lvl {self.lvl} and has {self.hp} hp." # Returns a string with the pokemons statistics.
  
class FirePokemon(Pokemon):
  def __init__(self, name, lvl):
    super().__init__(name, lvl)       # Calls the parent Classes __init__
  
  def ember(self):
    dmg = 75
    return f"{self.name} used Ember and dealt {dmg} amount of damage!"
  
class WaterPokemon(Pokemon):
  def __init__(self, name, lvl):
    super().__init__(name, lvl)
  
  def watergun(self):
    dmg = 60
    return f"{self.name} used Water Gun and dealt {dmg} amount of damage!"

class GrassPokemon(Pokemon):
  def __init__(self, name, lvl):
    super().__init__(name, lvl)
  
  def vinewhip(self):
    dmg = 50
    return f"{self.name} used Vine Whip and dealt {dmg} amount of damage!"

bulbasaur = GrassPokemon("Bulbasaur", 5)
charmander = FirePokemon("Charmander", 5)
squirtle = WaterPokemon("Squirtle", 5)

print(charmander.stats())             # Prints the value returned in the specified method.
print(charmander.ember())

print(squirtle.stats())
print(squirtle.watergun())

print(bulbasaur.stats())
print(bulbasaur.vinewhip())