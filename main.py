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
    keiko = Mammal("Keiko", "Whale", 27, "Carnivore", "water")

    # Creating health issue objects

    broken_leg = HealthIssue("Broken leg", date.today(), 3, "Rest 6 weeks")
    simba.add_health_issue(broken_leg)

    gastro = HealthIssue("Gastro", date.today(), 1, "Needs meds")
    rio.add_health_issue(gastro)

    splinter = HealthIssue("Splinter", date.today(), 2, "Extraction")
    kaa.add_health_issue(splinter)

    laceration = HealthIssue("Laceration", date.today(), 5, "Surgery")
    keiko.add_health_issue(laceration)

    # Create Enclosure objects

    aquarium = Aquarium("Marine", "water", 2000)
    aviary = Aviary("Sky", "sky", 300)
    vivarium = Vivarium("Jungle", "land", 2500)

    # Adding animals to enclosures

    aviary.add_animal(rio)
    vivarium.add_animal(simba)
    vivarium.add_animal(kaa)
    aquarium.add_animal(keiko)

    simba.assign_enclosure(vivarium.get_name())
    rio.assign_enclosure(aviary.get_name())
    kaa.assign_enclosure(vivarium.get_name())
    keiko.assign_enclosure(aquarium.get_name())

    # Creating Staff objects

    irwin = Zookeeper("Irwin", "Zookeeper")
    doolittle = Veterinarian("Doolittle", "Veterinarian")

    # Performing roles

    # Feeding

    print(irwin.feed_animal(simba))
    print(irwin.feed_animal(rio))

    # Cleaning

    print(irwin.clean_enclosure(vivarium))
    print(irwin.clean_enclosure(aviary))

    # Health Check

    print(doolittle.check_health(simba))
    print(doolittle.check_health(keiko))

    # Start Treatment

    broken_leg.start_treatment("Applied Cast")
    gastro.start_treatment("Supplied Meds")

    # Finish Treatment

    broken_leg.finish_treatment("Cast Removed, Healed")
    gastro.finish_treatment("Finished Meds, All Better")

if __name__ == '__main__':
    main()





