'''
File: main.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from datetime import date
from animal import Mammal, Bird, Reptile, HealthIssue
from enclosure import Aquarium, Aviary, Vivarium
from staff import Zookeeper, Veterinarian

def main():

    # Creating Animal objects

    simba = Mammal("Simba", "Lion", 5, "Carnivore", "land")
    rio = Bird("Rio", "Parrot", 3, "Herbivore", "sky")
    kaa = Reptile("Kaa", "Snake", 5, "Carnivore", "land")

    # Creating health issue objects

    broken_leg = HealthIssue("Broken leg", date.today(), 3, "Rest 6 weeks")
    simba.add_health_issue(broken_leg)

    gastro = HealthIssue("Gastro", date.today(), 3, "Needs meds")
    rio.add_health_issue(gastro)

    splinter = HealthIssue("Splinter", date.today(), 3, "Extraction")
    kaa.add_health_issue(splinter)