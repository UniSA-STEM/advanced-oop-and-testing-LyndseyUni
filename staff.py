'''
File: staff.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, role):
        if not name or isinstance(name, str):
            raise ValueError("Name must be a string")
        if not role or isinstance(role, str):
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
        return f"Staff Member: {self.__name} ({self.__role})}"

# Concrete Subclasses

class Zookeeper(Staff):
    def perform_duty(self):
        return f"{self.get_name()} is looking after the Zoo"

class Veterinarian(Staff):
    def perform_duty(self):
        return f"{self.get_name()} is looking after the Animals"

# Test suite to test the objects, methods and validation of the Staff class and subclasses

# Testing the Zookeeper creation

def test_staff_classes():
    zookeeper = Zookeeper("Irwin", "Zookeeper")
    assert zookeeper.get_name() == "Irwin"
    assert zookeeper.get_role() == "Zookeeper"
    assert str(zookeeper) == "Staff Member: Irwin (Zookeeper)"
    assert "feeding" in zookeeper.perform_duty()

# Testing the Veterinarian creation

    vet = Veterinarian("DooLittle", "Veterinarian")
    assert vet.get_name() == "DooLittle"
    assert vet.get_role() == "Veterinarian"
    assert "treating" in vet.perform_duty()

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
    test_staff_classes()
