
class Monster():


    name = None

    def __init__(self, name, life, damage):
        self.name = name
        self.life = life
        self.damage = damage

    def attack(self):
        return self.damage

    def receive_damage(self, amount):
        self.life = self.life - amount


    def get_name(self):
        return self.name


    def get_life(self):
        return self.life


    def get_damage(self):
        return self.damage

    def set_name(self, new_name):
        self.name = new_name

    def set_life(self, new_life):
        self.life= new_life

    def set_damage(self, new_damage):
        self.damage = new_damage

    @classmethod
    def set_name_for_all(cls, new_name):
        cls.name = new_name

    @classmethod
    def get_cls_name(cls):
        return cls.name
