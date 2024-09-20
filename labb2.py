class Pokemon():
  def __init__(self, name, lvl):
    self.name = name
    self.lvl = lvl
    self.hp = 100
  
  def stats(self):
    print(f"{self.name} is lvl {self.lvl} and has {self.hp} hp.")
  
class FirePokemon():
  def __init__(self, name, lvl):
    super("Pokemon").__init__(name, lvl)
  
  def fireattack(self):

    