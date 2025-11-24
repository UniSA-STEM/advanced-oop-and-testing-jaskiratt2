'''
File: zookeeper.py
Description: Represents the zookeper class where the person performes his role from staff
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        # call the parent class
        super().__init__(name, "zookeeper")

# Zookeeper feeds animal
    def feed_animal(self, animal):
        return self.get_name() + " will feed " + animal.get_name() + ": " + animal.eat()

# Zookeeper cleans enclosure
    def clean_enclosure(self, enclosure):
        answer = enclosure.clean()
        return self.get_name() + " has cleaned " + enclosure.get_id() + ": " + answer
