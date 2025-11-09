'''
File: staff.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

# Create the Staff class

class Staff(ABC):
    def __init__(self, name, role):

        # Data validation and exception handling

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a string")
        if not isinstance(role, str) or not role.strip():
            raise ValueError("Role must be a string")
        self.__name = name
        self.__role = role

    @abstractmethod
    def perform_duty(self):
        pass

    # Getters

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def __str__ (self):
        return f"Staff Member: {self.__name} ({self.__role})"

# Adding concrete subclasses to the Staff class using inheritance and polymorphism

class Zookeeper(Staff):
    def perform_duty(self):
        return f"{self.get_name()} is looking after the Zoo"

    def feed_animal(self, animal):
        try:
            animal.eat("food")
        except AttributeError:
            return f"{animal} cannot be fed"
        return f"{self.get_name()} fed {animal.get_name()} the {animal.get_species()}"

    def clean_enclosure(self, enclosure):
        try:
            enclosure.clean_enclosure()
        except AttributeError:
            return f"{enclosure} cannot be cleaned"
        return f"{self.get_name()} cleaned the {enclosure.get_name()} enclosure"

class Veterinarian(Staff):
    def perform_duty(self):
        return f"{self.get_name()} is looking after the Animals"

    def check_health(self, animal):
        return f"{self.get_name()} checked {animal.get_name()}'s health"

# Test suite to test the objects, methods and validation of the Staff class and subclasses

# Testing the Zookeeper creation

def test_staff_classes():
    zookeeper = Zookeeper("Irwin", "Zookeeper")
    assert zookeeper.get_name() == "Irwin"
    assert zookeeper.get_role() == "Zookeeper"
    assert zookeeper.perform_duty() == "Irwin is looking after the Zoo"
    print(zookeeper)

# Testing the Veterinarian creation

    vet = Veterinarian("DooLittle", "Veterinarian")
    assert vet.get_name() == "DooLittle"
    assert vet.get_role() == "Veterinarian"
    assert vet.perform_duty() == "DooLittle is looking after the Animals"
    print(vet)

# Exception Handling

    try:
        Zookeeper(" ", "Zookeeper")
        assert False, "Expected exception"
    except ValueError:
        pass

    try:
        Veterinarian("DooLittle ", " ")
        assert False, "Expected exception"
    except ValueError:
        pass

if __name__ == "__main__":
    from animal import Mammal
    from enclosure import Vivarium
    lion = Mammal("Simba", "Lion", 5, "Carnivore", "land")
    vivarium = Vivarium("Tanzania", "land", 500)
    keeper = Veterinarian("DooLittle", "Veterinarian")
    print("Staff tests passed successfully")

