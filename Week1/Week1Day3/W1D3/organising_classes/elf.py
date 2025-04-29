from organising_classes.character import Character

class Elf(Character):#!Inheritance
    def __init__(self, name):
        super().__init__(name)#!Inheritance
    # !Polymorphism
    def magic_attack(self, enemy):
        enemy.health -= self.power
        enemy.power -= 20
        enemy.defense -= 10