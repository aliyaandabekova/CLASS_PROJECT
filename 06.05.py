class Human:
    def __init__(self,name,age,weight,height,gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.soul = True
        self.viruses = []
        self.health = 100
    # def __str__(self):
    #     return self.name + str(self.age)
    def __repr__(self):
        return self.name
    def add_viruse(self,viruse):
        if viruse not in self.viruses:
            self.viruses.append(viruse)
            self.health -= 10

human1 = Human(name='John',age = 48,weight=90,height=185,gender='M')
human2 = Human(name='Sue',age = 48,weight=90,height=185,gender='M')
human3 = Human(name='Hue',age = 48,weight=90,height=185,gender='M')
humans= [human1,human2,human3]

human1.add_viruse('covid')
human1.add_viruse('plague')

print(human1.health)
print(human1.__dict__)