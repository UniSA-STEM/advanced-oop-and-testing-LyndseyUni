'''
File: animal.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Health Issue class to record each animals health

from datetime import date

class HealthIssue:
    def __init__(self, description, reported_on, severity, treatment_notes=""):
        # data validation
        if not description or not isinstance (description, str):
            raise ValueError("Description must be a string")
        if not isinstance (reported_on, date):
            raise ValueError("Reported_on must be a date")
        if not isinstance (severity, int) or not (1 <= severity <= 5):
            raise ValueError("Severity must be between 1 and 5")

        # Health Issue private attributes
        self.__description = description
        self.__reported_on = reported_on
        self.__severity = severity
        self.__treatment_notes = False

    # Health Issue Methods
    def start_treatment(self, notes=""):
        self.__treatment_notes = True
        if notes:
            self.__treatment_notes += ("\n" + notes) if self.__treatment_notes else notes

    def finish_treatment(self, notes=""):
        self.__under_treatment = False
        if notes:
            self.__treatment_notes += ("\n" + notes) if self.__treatment_notes else notes

    def to_zoo_log(self):
        return {
            "description" : self.__description,
            "reported_on" : self.__reported_on,
            "severity" : self.__severity,
            "treatment_notes" : self.__treatment_notes,
            "under_treatment" : self.__under_treatment,
        }
    # Getters
    def get_description(self):
        return self.__description

    def get_reported_on(self):
        return self.__reported_on

    def get_severity(self):
        return self.__severity

    def get_treatment_notes(self):
        return self.__treatment_notes