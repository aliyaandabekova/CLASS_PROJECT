class Flora:
    def __init__(self, name, lifespan, habitat, plant_type):
        self.name = name
        self.lifespan = lifespan
        self.habitat = habitat
        self.plant_type = plant_type
        self.size = 0

class Fauna:
    def __init__(self, name):
        self.name = name

class Predactor(Fauna):
    def __init__(self,name):
        super().__init__(name)

class Mammals(Fauna):
    def __init__(self, name):
        super().__init__(name)

dog = Mammals('dog')
print(dog.__dict__)