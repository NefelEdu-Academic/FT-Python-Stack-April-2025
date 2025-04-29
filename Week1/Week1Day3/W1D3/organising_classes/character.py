class Character:
    # !Encapsulation
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 50
        self.defense = 30
        self.weapon = None
    
    def attack(self, target):
        print(f"[Attack] {self.name} attacked {target.name}")
        final_damage = target.defend(self.power) #!Abstraction
        print(f"AND cause Damage = {final_damage}")
        target.health -= final_damage
        return self
        
    def defend(self, damage):
        print(f"[Defend] {self.name} defended {damage} AND reduce it by {self.defense}")
        damage -= self.defense
        return damage