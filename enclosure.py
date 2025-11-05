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
from datetime import datetime

# Create the Enclosure class

class Enclosure(ABC):
    def __init__(self, name: str, enc_type: str, size: int):

        # data validation and exception handling

        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not enc_type or not isinstance (enc_type, str):
            raise ValueError("Enc_type must be a string")
        if not isinstance (size, int):
            raise ValueError("Size must be an integer")

    # Enclosure class private attributes

        self.__name = name
        self.__enc_type = enc_type
        self.__cleanliness = 100
        self.__animals = []
        self.__last_cleaned = None
        self.__feeding_log = []

    # Abstract Methods

    @abstractmethod
    def is_suitable(self, animal) -> bool:
        pass

    @abstractmethod
    def clean_enclosure(self):
        pass

    @abstractmethod
    def feed_animal(self):
        pass






