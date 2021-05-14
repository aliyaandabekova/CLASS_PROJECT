class Armor:

    def __init__(self,name,power,health,defense,stamina):
        self.name = name
        self.power = power
        self.health = health
        self.defense = defense
        self.stamina = stamina
        self.__armor_type = None

    def armor_type(self,type):
        if type == 'rare':
            self.power *= 1.1
        elif type == 'legendary':
            self.power *= 1.7
        self.__armor_type = type


