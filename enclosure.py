'''
File: filename.py
Description: A brief description of this Python module.
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    if enclosure_id == "":
        print("Error: Sorry! Enclosure ID can't be empty.")
        return
    if size <=0:
        print("Error: Sorry! Size needs to be greater than 0.")

    self.__id = enclosure_id
    self.__size = size
    self.__environment = environment
    self.__animal = []
    self.__cleanliness = 100

def get_id(self):
    return self.__id
def get_size(self):
    return self.__size
def get_environment(self):
    return self.__environment
def get_animal(self):
    return self.__animal
def get_cleanliness(self):
    return self.__cleanliness

def add_animal(self, animal):
    self.__animal.append(animal)
def remove_animal(self, animal):
    if animal in self.__animal:
        self.__animal.remove(animal)
