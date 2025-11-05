'''
File: enclosure.py
Description: Assignment: Advanced Programming
Author: Lyndsey Threlfall
ID: Thrly001@mymail.unisa.edu.au
Username: thrly001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Imports

from animal import Animal
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
        self.__animals = []
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
        if not self.__is_suitable:
            raise ValueError(f"Enclosure '{animal.get_species()}' cannot live in {self.__enc_type}")
        self.__animals.append(animal)

    # Removes an animal from the enclosure

    def remove_animal(self, animal: Animal):
        if animal in self.__animals:
            self.__animals.remove(animal)

    # Updates the enclosures cleanliness status

    def clean(self):
        self.__cleanliness = "Clean"

    # Creates and returns a dictionary recording all the key information about an enclosure

    def enc_info(self):
        return {
            "name": self.__name,
            "enclosure": self.__enc_type,
            "size": self.__size,
            "cleanliness": self.__cleanliness,
            "animals": [str(a) for a in self.__animals],
        }











