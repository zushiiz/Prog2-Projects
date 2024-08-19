import random

def dmgcalc(atk):
    crit = random.randint(1, 16)
    if crit == 1:
        dmg = atk * 2
        return dmg
    else:
        dmg == atk
        return dmg
        
class pokemon():
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl

        self.atk = 10
        self.hp = 30
        self.spd = 30
        self.maxhp = self.hp
        self.evo = 1

    def stat(self):
        print(f"{self.name} Type:{self.type} LVL:{self.lvl} ATK:{self.atk} HP:{self.hp} SPD:{self.spd}")

    def trainatk(self):
        if self.lvl == 90:
            print(f"{self.name} has reached max LVL!")
        else:
            self.lvl += 1
            print(f"{self.name} is now lvl {self.lvl}! ATK increased from {self.spd} to {self.spd + 1}")
            self.atk += 1
            print(f"{self.name} is now lvl {self.lvl}!")
    def trainhp(self):
        if self.lvl == 90:
            print(f"{self.name} has reached max LVL!")
        else:   
            self.lvl += 1
            print(f"{self.name} is now lvl {self.lvl}! HP increased from {self.spd} to {self.spd + 1}")
            self.hp += 2
    def trainspd(self):
        if self.lvl == 90:
            print(f"{self.name} has reached max LVL!")
        else:        
            self.lvl += 1
            print(f"{self.name} is now lvl {self.lvl}! SPD increased from {self.spd} to {self.spd + 1}")        
            self.spd += 1

    def evolve(self, new_name):
        if self.evo == 3:
            print(f"{self.name} cannont evolve anymore!")
        elif self.lvl < 16 and self.evo == 1:
            print(f"{self.name} is not high enough LVL!")
        elif self.lvl < 32 and self.evo == 2:
            print(f"{self.name} is not high enough LVL!")        
        else:
            print(f"{self.name} has evolved into {new_name}!")
            self.name = new_name
            self.evo += 1
            self.atk *= 1.2
            self.hp *= 1.2
            self.spd *= 1.1
            self.atk = round(self.atk)
            self.hp = round(self.hp)
            self.spd = round(self.spd)

    def maxheal(self):
        self.hp = self.maxhp
        print(f"{self.name} is now at max HP {self.hp}!")
    def alive(self):
        if self.hp > 0:
            print(f"{self.name} is alive!")    

    def attack(self, enemy):
        if self.spd > enemy.spd:
            dmg = dmgcalc(self.atk)
            enemy.hp -= dmg
            dmg = dmgcalc(enemy.atk)
            self.hp -= dmg

        else:
            dmg = dmgcalc(enemy.atk)
            self.hp -= dmg            
            dmg = dmgcalc(self.atk)
            enemy.hp -= dmg

            
        print(f"{self.name} attacks {enemy.name} and did {self.lvl} amount of damage!")

charmander = pokemon("Charmander", "Fire", 1)
bulbasaur = pokemon("Bulbasaur", "Grass", 1)

charmander.attack(bulbasaur)
