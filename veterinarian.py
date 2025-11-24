'''
File: veterinarian.py
Description: Represents a vet doctor class that treats and add health record of animals
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from health_record import HealthRecord
from staff import Staff

class Veterinarian(Staff):
    def __init__(self, name):
        # set the parent staff class
        super().__init__(name, "Veterinarian")
# main job of vet to treat sick animals
    def treat_animal(self, animal, description, date, severity, treatment=""):
        record = HealthRecord(description, severity, date, treatment)
        #add record to the animals health history
        animal.add_health_record(record)
        # treatment got saved
        return "Treatment is recorded for " + animal.get_name()
