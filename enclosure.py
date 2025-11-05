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

class Enclosure:
    def __init__(self, name, enc_type, size):

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
        self.__cleanliness = "Clean"
        self.__animals = []





