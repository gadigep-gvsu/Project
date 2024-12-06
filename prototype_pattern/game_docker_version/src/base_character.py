import copy

class GameCharacter:
    def __init__(self, name, health, weapons):
        self.name = name
        self.health = health
        self.weapons = weapons.copy()
    
    def clone(self):
        return copy.deepcopy(self)
    
    def take_damage(self, damage):
        self.health -= damage
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("Weapons: " + ", ".join(self.weapons))
        print("---")