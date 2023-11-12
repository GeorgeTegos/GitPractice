from lineage.models.FirstClass import FirstClass

class SecondClass(FirstClass):

    def __init__(self, name, race, gender, _class, grade):
        super().__init__(name, race, gender, _class, grade)