'''
File: animal.py
Description: The main parent class for all animals in the zoo
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

        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health_records = []
# simple getters
    def get_name(self):
        return self.__name
    def get_species(self):
        return self.__species
    def get_age(self):
        return self.__age
    def get_dietary_needs(self):
        return self.__dietary_needs
    def get_health_records(self):
        return self.__health_records
# basic animals behaviours
    def make_sound(self):
        return f"{self.__name} make a sound"
    def eat(self):
        return f"{self.__name} is eating {self.__dietary_needs}"
    def sleep(self):
        return f"{self.__name} is sleeping"
# vet uses thus to add health problem
    def add_health_record(self, record):
        self.__health_records.append(record)

    def is_under_treatment(self):
        for record in self.__health_records:
             if record.get_severity() in ["high", "emergency"] and not record.is_resolved():
                return True
        return False