
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, self.damage)
        if self.health <= 0:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"
        pass


class Saxon(Soldier):

    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(self.damage)
        if self.health <= 0:
            return "A Saxon has died in combat"


# War

class War:
    def __init__(self,):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
