'''
File: bird.py
Description: Represents all bird animals in the zoo
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs):
        # setup the parents animal class for name,age etc
        super().__init__(name, species, age, dietary_needs)

    # all mammals make the sound
    def make_sound(self):
        return f"{self.get_name()} chirps"