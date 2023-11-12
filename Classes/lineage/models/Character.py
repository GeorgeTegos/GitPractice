#Properties/Attributes : Race - Class - Gender - Name - hp - mana
#methods : walk() - sit() - attack()

class Character():

    def __init__(self,name, race, gender, _class):
        self.name = name
        self.race = race
        self.gender = gender
        self._class = _class
        self.hp = 300
        self.mana = 200
        self.skills = []

    def show_char_info(self):
        list = self.my_skills()
        print(f"I am {self.name}, my race is {self.race} my class is {self._class} "
              f"and I am {self.gender} and my skills are {list}")

    def change_name(self,new_name):
        self.name = new_name
    def add_skill(self, banana):
        self.skills.append(banana)
    def my_skills(self):
        return_skills_name = []
        for skill in self.skills:
            return_skills_name.append(skill.name)
            # print(f"{skill.name} ")
        return return_skills_name

    def skill_attack(self, skill):
        self.mana = self.mana - skill.mana_cost
        return skill.power

    def receive_damage(self, amount):
        self.hp = self.hp - amount
