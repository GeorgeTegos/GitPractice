from lineage.models.Character import Character

class FirstClass(Character):

    def __init__(self, name, race, gender, _class, grade):
        super().__init__(name, race, gender, _class)
        self.grade = grade

