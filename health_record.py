'''
File: health_record.py
Description: This class saves health problem for an animal
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    def __init__(self, description, severity, data_reported, treatment_plan=""):
        if description == "":
            print("Error: Sorry! Health description is empty.")
            return
        if severity not in ["low", "medium", "high", "emergency"]:
            print("Error: Sorry! Health severity can only be 'low', 'medium', 'high' or 'emergency'.")
            return
# store all required health information
        self.__description = description
        self.__severity = severity
        self.__data_reported = data_reported
        self.__treatment = treatment_plan
        self.__resolved = False
# allows other classes to read health info
    def get_description(self):
        return self.__description
    def get_severity(self):
        return self.__severity
    def get_data_reported(self):
        return self.__data_reported
    def get_treatment_plan(self):
        return self.__treatment
    def is_resolved(self):
        return self.__resolved
    # health issue marked resolved
    def resolve(self):
        self.__resolved = True
# displays the health record
    def show_record(self):
        if self.__resolved:
            answer = "Resolved"
        else:
            answer = "Active"
        print("[" + self.__data_reported + "] " + self.__severity + ": " + self.__description + "[" + answer + "]")
