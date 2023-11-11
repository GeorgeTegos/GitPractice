#Properties/Attributes : Race - Class - Gender - Name
#methods : walk() - sit() - attack()
from lineage.models.Character import Character
from lineage.models.Skill import Skill
from lineage.models.Monster import Monster


# name - power - mana_cost - type

playerOne = Character("QueenBee","Elf","Female","Mage")
playerTwo = Character("GTultimate","Human","Male","Fighter")


skillOne = Skill("Wind Strike",9,5,"Magic")
skillTwo = Skill("Power Strike", 12,10,"Physical")


playerOne.add_skill(skillOne)
playerTwo.add_skill(skillTwo)

# Obj/Instance          Object - attributes/properties
monsterOne      =       Monster("Gremlin", 40, 5)

print(monsterOne) # <lineage.models.Monster.Monster object at 0x108dd1350>
print(monsterOne.name)  # Gremlin


playerDamage = playerOne.skill_attack(skillOne)





