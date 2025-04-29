from organising_classes.character import Character

class Barbarian(Character): #!Inheritance 
    def __init__(self, name):
        super().__init__(name)#!Inheritance
        self.power += 30 #!Polymorphism
        self.health += 50 #!Polymorphism
        self.rage = 30 #!Encapsulation : adds a new attribute specific to Barbarian
        