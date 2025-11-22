'''
File: animal.py
Description: A brief description of this Python module.
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, dietary_needs):
        if name == "":
            print("Error: Sorry!! Animal's name cannot be empty.")
            return
        if age < 0:
            print("Error: Sorry!! Age cannot be negative.")
            return
        if dietary_needs == "":
            print("Error: Sorry!! Dietary needs to be provided.")
            return

        self.name = name
        self.species = species
        self.age = age
        self.dietary_needs = dietary_needs
        self.health_records = []

    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def get_age(self):
        return self.age
    def get_dietary_needs(self):
        return self.dietary_needs
    def get_health_records(self):
        return self.health_records

    def make_sound(self):
        return f"{self.name} make a sound"
    def eat(self):
        return f"{self.name} is eating {self.dietary_needs}"
    def sleep(self):
        return f"{self.name} is sleeping"