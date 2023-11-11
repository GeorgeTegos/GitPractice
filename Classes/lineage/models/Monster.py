
class Monster():

    def __init__(self, name, life, damage):
        self.name = name
        self.life = life
        self.damage = damage

    def attack(self):
        return self.damage

    def receive_damage(self, amount):
        self.life = self.life - amount
