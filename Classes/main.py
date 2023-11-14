#Properties/Attributes : Race - Class - Gender - Name
#methods : walk() - sit() - attack()
from lineage.models.Character import Character
from lineage.models.Skill import Skill
from lineage.models.Monster import Monster
from lineage.models.FirstClass import FirstClass
from lineage.models.SecondClass import SecondClass


# name - power - mana_cost - type

playerOne = Character("QueenBee","Elf","Female","Mage")
playerTwo = Character("GTultimate","Human","Male","Fighter")


skillOne = Skill("Wind Strike",9,5,"Magic")
skillTwo = Skill("Power Strike", 12,10,"Physical")


playerOne.add_skill(skillOne)
playerTwo.add_skill(skillTwo)

# Obj/Instance          Object - attributes/properties
monsterOne      =       Monster("Gremlin", 40, 5)
monsterTwo = Monster("Wolf", 80, 8)

# print(monsterOne) # <lineage.models.Monster.Monster object at 0x108dd1350>
# print(monsterOne.name)  # Gremlin

print(f"Player's life before battle: {playerOne.hp}")
print(f"Monster's life before battle: {monsterOne.life}")

def combat_pve(player, monster):
# repeat this until monster or player dies
    while player.hp > 0 and monster.life >0:
# player attacks with skill
        player_damage = player.skill_attack(player.skills[0])
# monster loses life from skill power

        monster.receive_damage(player_damage)

# monster attacks player
        monster_damage = monster.attack()
# player loses life from monster's damage
        player.receive_damage(monster_damage)
    print(f"Player life: {player.hp} and Monster life: {monster.life}")

combat_pve(playerOne, monsterOne)
combat_pve(playerOne, monsterTwo)

elf_mage = FirstClass("QueenBee","Elf","Female","Elf Mage","D")
print(elf_mage.grade)

elf_mage.add_skill(skillOne)
print(elf_mage.my_skills())

Spellsinger = SecondClass("QueenBee", "Elf", "Female", "Spellsinger" , "C")
print(Spellsinger.gender)


print(monsterOne.get_name())