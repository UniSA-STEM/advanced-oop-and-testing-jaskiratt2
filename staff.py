'''
File: filename.py
Description: A brief description of this Python module.
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__ (self,name,role):
        if name == "":
            print("Error: Sorry! There should be a staff name everytime")
            return
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def work(self):
        return self.__name + " works as " + self.__role
    def __str__(self):
        return self.__name + " (" + self.__role + ")"