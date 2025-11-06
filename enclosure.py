'''
File: enclosure.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Imports

from animal import Animal, Mammal, Bird, Reptile
from abc import ABC, abstractmethod
from typing import List

# Create the Enclosure class

class Enclosure(ABC):
    def __init__(self, name: str, enc_type: str, size: int):

        # data validation and exception handling

        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not enc_type or not isinstance (enc_type, str):
            raise ValueError("Enc_type must be a string")
        if not isinstance (size, int) or size <= 0:
            raise ValueError("Size must be an integer")

    # Enclosure class private attributes

        self.__name = name
        self.__enc_type = enc_type
        self.__size = size
        self.__cleanliness = "Clean"
        self.__animals: List[Animal] = []
        self.__cleaning_log: List[str] = []
        self.__feeding_log: List[str] = []

    # Abstract Methods

    @abstractmethod
    def is_suitable(self, animal: Animal) -> bool:
        pass

    @abstractmethod
    def daily_routine(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass

    @abstractmethod
    def clean_enclosure(self):
        pass

    @abstractmethod
    def feed_animal(self):
        pass

    # Concrete methods with data validation and exception handling

    # Keeps a record of each feed

    def feed_log(self, note="Fed"):
        self.__feeding_log.append(note)

    # Keeps a record of each clean

    def clean_log(self, note="Cleaned"):
        self.__cleaning_log.append(note)
        self.__cleanliness = "Clean"

    # Adds an animal to the enclosure if they pass two checks:
    # (if the enclosure is not full and the animal is suitable for the enclosure)

    def add_animal(self, animal: Animal):
        if len(self.__animals) >= self.__size:
            raise ValueError(f"Enclosure '{self.__name}' is full")
        if not self.__is_suitable(animal):
            raise ValueError(f"Enclosure '{animal.get_species()}' cannot live in {self.__enc_type}")
        self.__animals.append(animal)
        animal.set_assigned_enclosure(self)

    # Removes an animal from the enclosure

    def remove_animal(self, animal: Animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.unassign_enclosure()

    # Updates the enclosures cleanliness status

    def clean(self):
        self.clean_log("Cleaned")

    # Getters

    def get_animal(self):
        return self.__animals.copy()

    def get_cleanliness(self):
        return self.__cleanliness

    # Creates and returns a dictionary recording all the key information about an enclosure

    def enc_info(self):
        return {
            "name": self.__name,
            "enclosure": self.__enc_type,
            "size": self.__size,
            "cleanliness": self.__cleanliness,
            "animals": [str(a) for a in self.__animals],
            "feeding_log": self.__feeding_log,
            "cleaning_log": self.__cleaning_log,
        }
# Adding concrete subclasses to the Enclosure class using inheritance and polymorphism

class Aquarium(Enclosure):
    def is_suitable(self, animal: Animal) -> bool:
        return animal.get_category().lower() == "aquatic"

    def daily_routine(self):
        self.feed_animal()
        self.clean_enclosure()

    def generate_report(self):
        print("--- Aquarium Report ---")
        for key, value in self.enc_info().items():
            print(f"{key}: {value}")

    def clean_enclosure(self):
        self.clean_log("Cleaned Aquarium")

    def feed_animal(self):
        self.feed_animal()

class Aviary(Enclosure):
    def is_suitable(self, animal: Animal) -> bool:
        return animal.get_category(self) == "bird"

    def daily_routine(self):
        self.feed_animal()
        self.clean_enclosure()

    def generate_report(self):
        print("--- Aviary Report ---")
        for key, value in self.enc_info().items():
            print(f"{key}: {value}")

    def clean_enclosure(self):
        self.clean_log("Cleaned Aviary")

    def feed_animal(self):
        for animal in self.__animals():
           animal.eat("seeds")
           self.feed_log(f"Fed {animal.get_species()}")

class Vivarium(Enclosure):
    def is_suitable(self, animal: Animal) -> bool:
        return animal.get_category() == "land"

    def daily_routine(self):
        self.feed_animal()
        self.clean_enclosure()

    def generate_report(self):
        print("--- Vivarium Report ---")
        for key, value in self.enc_info().items():
            print(f"{key}: {value}")

    def clean_enclosure(self):
        self.clean_log("Cleaned Vivarium")

    def feed_animal(self):
        for animal in self.get_animals():
            self.feed_log(f"Fed {animal.get_species()}")

class TestAnimal(Animal):
    def make_sound(self):
        return "Test Sound"

# Test suite to test the objects, methods and validation of the Enclosure class and subclasses

def test_aquarium_suitability():
    aquarium = Aquarium("Water", "Aquarium", 20)
    fish = Fish("Freddy", "Fish", 2, "Omnivore", "aquatic")
    turtle = Reptile("Raphael", "Turtle", 15, "Pizza", "aquatic")
    assert aquarium.is_suitable(fish)
    aquarium.add_animal(fish)
    aquarium.add_animal(turtle)
    assert len(aquarium.get_animals()) == 20

def test_aquarium_is_correct_enclosure():
    aquarium = Aquarium("Water", "Aquarium", 20)
    lion = Mammal("Simba", "Lion", 5, "Carnivore", "land")
    error_raised = False
    try:
        aquarium.add_animal(lion)
    except ValueError:
        error_raised = True
    assert error_raised, "Wrong Animal Type"

if __name__ == "__main__":
    fish = TestAnimal("Freddy", "Fish", 2, "Omnivore", "aquatic")
    bird = TestAnimal("Rio", "Parrot", 3, "Herbivore", "air" )
    reptile = TestAnimal("Kaa", "Python", 10, "Carnivore", "land")
    aquarium = Aquarium("Pond", "Water", 10)
    aviary = Aviary("Forrest", "Air", 25)
    vivarium = Vivarium("Reptile House", "Land", 30)
    assert aquarium.is_suitable(fish)
    assert aviary.is_suitable(Bird)
    assert vivarium.is_suitable(reptile)
    aquarium.clean_log("Cleaned Aquarium")
    aquarium.feed_log("Fed")
    assert len(aquarium._Enclosure__cleaning_log) == 1
    assert len(aquarium._Enclosure__feeding_log) == 1
    aquarium.remove_animal(fish)
    assert fish not in aquarium._Enclosure__animals
    print("Enclosure Tests Passed Successfully")












