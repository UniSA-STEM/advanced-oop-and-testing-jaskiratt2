from health_record import HealthRecord
from staff import Staff

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def treat_animal(self, animal, description, date, severity, treatment=""):
        record = HealthRecord(description, severity, date, treatment)
        animal.add_health_record(record)
        return "Treatment is recorded for " + animal.get_name()
