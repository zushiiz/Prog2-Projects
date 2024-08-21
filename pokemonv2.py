import random

pokemon_types = {
  "normal": [],
  "fire": ["grass", "ice", "bug", "steel"],
  "water": ["fire", "ground", "rock"],
  "electric": ["water", "flying"],
  "grass": ["water", "ground", "rock"],
  "ice": ["grass", "ground", "flying", "dragon"],
  "fighting": ["normal", "ice", "rock", "dark", "steel"],
  "poison": ["grass", "fairy"],
  "ground": ["fire", "electric", "poison", "rock", "steel"],
  "flying": ["grass", "fighting", "bug"],
  "psychic": ["fighting", "poison"],
  "bug": ["grass", "psychic", "dark"],
  "rock": ["fire", "ice", "flying", "bug"],
  "ghost": ["psychic", "ghost"],
  "dragon": ["dragon"],
  "dark": ["psychic", "ghost"],
  "steel": ["ice", "rock", "fairy"],
  "fairy": ["fighting", "dragon", "dark"]
}

class pokemon():
    def __init__(self, name, type1, type2, lvl, baseatk, basehp, basedef, basespd, evostg):
        self.name = name
        self.type1 = type1
        self.typ2 = type2
        self.lvl = lvl
        self.baseatk = baseatk
        self.basehp = basehp
        self.basedef = basedef
        self.basespd = basespd
        self.evostg = evostg

        self.maxhp = basehp
        