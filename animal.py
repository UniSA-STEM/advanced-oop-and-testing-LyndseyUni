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
        # data validation and exception handling
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
        self.__treatment_notes = treatment_notes
        self.__under_treatment = False

    # Health Issue Methods

    # tells if the animal is under treatment and optionally adds or appends their treatment notes

    def start_treatment(self, notes=""):
        self.__under_treatment = True
        if notes:
            self.__treatment_notes += ("\n" + notes) if self.__treatment_notes else notes


    # shows the treatment is complete and optionally adds closing notes to their treatment notes

    def finish_treatment(self, notes=""):
        self.__under_treatment = False
        if notes:
            self.__treatment_notes += ("\n" + notes) if self.__treatment_notes else notes

    # Creates and returns a dictionary recording all the key information about a health issue

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

    def is_under_treatment(self):
        return self.__under_treatment

# Test suite to test the objects, methods and validation of the HealthIssue class

if __name__ == '__main__':
    from datetime import date
    issue = HealthIssue("Broken Leg", date.today(), 3, "Rest 6 Weeks")
    assert issue.get_severity() == 3
    issue.start_treatment("Cast Applied")
    assert issue.is_under_treatment() is True
    issue.finish_treatment("All Better")
    assert issue.is_under_treatment() is False
    print("HealthIssue tests completed successfully")




