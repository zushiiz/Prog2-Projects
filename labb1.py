class pokemon:
    def __init__(self, name, type, lvl, hp):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.hp = hp
        self.maxhp = hp
    def desc(self):
        print(f"{self.name} Type:{self.type} LVL:{self.lvl} HP:{self.hp}")
    def train(self):
        self.lvl += 1
        print(f"{self.name} is now lvl {self.lvl}!")
    def evolve(self, new_name):
        print(f"{self.name} has evolved into {new_name}!")
        self.name = new_name
    def attack(self, enemy):
        enemy.hp -= self.lvl
        print(f"{self.name} attacks {enemy.name} and did {self.lvl} amount of damage!")
    def heal(self):
        self.hp = self.maxhp
        print(f"{self.name} is now at max HP {self.hp}!")
    def alive(self):
        if self.hp > 0:
            print(f"{self.name} is alive!")

pikachu = pokemon("Pikachu", "Electric", 5, 100)

bulbasaur = pokemon("Bulbasaur", "Grass", 6, 100)

pikachu.desc()
bulbasaur.desc()
pikachu.train()
pikachu.desc()
bulbasaur.attack(pikachu)
pikachu.desc()
pikachu.heal()
pikachu.evolve("Raichu")
pikachu.desc()