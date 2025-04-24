from organising_classes.barbarian import Barbarian

class Seer:
    def __init__(self):
        self.__see_range=100 #!encapsulation
        self.hidden_type = Barbarian("Seer") #! Abstraction
        
    def get_see_range(self):
        return self.__see_range