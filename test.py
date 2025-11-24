'''
File: test.py
Description: This is the test file to pass all test i perform
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from veterinarian import Veterinarian

# Test 1 – Animal Sound

def test_animal_sounds():
    tommy = Mammal("tommy", "Lion", 3.5, "Meat")
    mithu = Bird("mithu", "Parrot", 1, "Seeds")
    simba = Reptile("simba", "Python", 3, "Mice")

    assert tommy.make_sound() == "tommy yowl"
    assert mithu.make_sound() == "mithu chirps"
    assert simba.make_sound() == "simba hisses"


# Test 2 – Adding Health Record

def test_vet_treatment():
    mithu = Bird("mithu", "Parrot", 1, "Seeds")
    vet = Veterinarian("Dr. Jaskirat")

    result = vet.treat_animal(mithu, "Wing got injured", "24-11-2025", "high", "Rest")


    assert result == "Treatment is recorded for mithu"
    assert len(mithu.get_health_records()) == 1

# Test 3 – Enclosure Add Animal

def test_enclosure_add():
    from enclosure import Enclosure

    tommy = Mammal("tommy", "Lion", 3.5, "Meat")
    grassland = Enclosure("2005", 400, "thick bushes")

    grassland.add_animal(tommy)


    assert len(grassland.get_animal()) == 1
    assert grassland.get_animal()[0].get_name() == "tommy"
