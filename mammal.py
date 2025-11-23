from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs )

    def make_sound(self):
        return f"{self.get_name()} yowl"
