from organising_classes.character import Character    
from organising_classes.barbarian import Barbarian    
from organising_classes.seer import Seer    
john = Character("John")
omen = Barbarian("Omen")
harry = Seer()


# john.attack(omen).attack(harry.hidden_type)
# omen.attack(john).attack(harry.hidden_type)
print(harry.get_see_range())