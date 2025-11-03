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

    # Tells if the animal is under treatment and optionally adds or appends their treatment notes

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

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species, age, diet):

        # data validation and exception handling

        if not name or not isinstance (name, str):
            raise ValueError("Name must be a string")
        if not isinstance (species, str):
            raise ValueError("Species must be a string")
        if not isinstance (age, int) or age <= 0:
            raise ValueError("Age must be a positive integer")
        if not diet or isinstance (diet, str):
            raise ValueError("Diet must be a string")

        # Animal class private attributes

        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_records = []
        self.__assigned_enclosure = None

    @abstractmethod
    def make_sound(self):
        pass

    # Methods of actions with exception handling

    # Ensures a food is entered and prompts if it is not

    def eat(self, food):
        if not food:
            raise ValueError("Food must be provided")
        return f"{self.__name} eats {food} {self.__diet}"

    # Ensures a number of hours of sleep is entered and prompts if not or if negative

    def sleep(self, hours):
        if not isinstance (hours, int) or hours <= 0:
            raise ValueError("Hours must be a positive integer")
        return f" {self.__name} sleeps for {hours} hours"

    # Health Methods and exception handling

    # Validates and stores a health issue in the animal's health records

    def add_health_issue(self, issue):
        if not isinstance (issue, HealthIssue):
            raise ValueError("Issue must be a HealthIssue")
        self.__health_records.append(issue)

    # Creates a health report and stores the animal's health issues in a list

    def health_report(self):
        return [issue.to_zoo_log() for issue in self.__health_records]

    # Returns True if the animal is under treatment False if treatment is finished

    def is_under_treatment(self):
        return any(issue.is_under_treatment() for issue in self.__health_records)

    # Methods for assigning / unassigning an enclosure for an Animal

    # Assigning an animal to an enclosure in the zoo

    def assign_enclosure(self, enclosure_name):
        self.__assigned_enclosure = enclosure_name

    # Unassigning an animal to an enclosure in the zoo

    def unassign_enclosure(self):
        self.__assigned_enclosure = None

    # Getters
    def get_name(self):
        return self.__name
    def get_species(self):
        return self.__species
    def get_age(self):
        return self.__age
    def get_diet(self):
        return self.__diet
    def get_assigned_enclosure(self):
        return self.__assigned_enclosure

    # String Conversion

    def __str__ (self):
        return f"{self.__name}, {self.__species}, {self.__age}"

# Adding concrete classes to the Animal class using inheritance and polymorphism

class Mammal(Animal):
    def make_sound(self):
        return f"{self.get_name()} the {self.get_species()} Growls"

class Bird(Animal):
    def make_sound(self):
        return f"{self.get_name()} the {self.get_species()} Tweets"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.get_name()} the {self.get_species()} Hisses"














