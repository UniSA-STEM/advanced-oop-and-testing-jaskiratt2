'''
File: main.py
Description: This is the main file where i run my code
Author: Jaskirat Uppal
ID: 110426141
Username: uppjy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from health_record import HealthRecord
from zoo import Zoo

# Create the zoo
my_zoo = Zoo("Simone's Lovely Zoo")

# Create animals
tommy = Mammal("tommy", "Lion", 3.5, "Meat")
mithu = Bird("mithu", "Parrot", 1, "Seeds")
simba = Reptile("simba", "Python", 3, "Mice")

my_zoo.add_animal(tommy)
my_zoo.add_animal(mithu)
my_zoo.add_animal(simba)

# Create enclosures
grassland = Enclosure("2005", 400, "thick bushes")
rainforest = Enclosure("3362", 150, "forest")
reptile_house = Enclosure("6435", 75, "desert")

grassland.add_animal(tommy)
rainforest.add_animal(mithu)
reptile_house.add_animal(simba)

my_zoo.add_enclosure(grassland)
my_zoo.add_enclosure(rainforest)
my_zoo.add_enclosure(reptile_house)


piyush = Zookeeper("Piyush")                    # Zookeeper
dr_jaskirat = Veterinarian("Dr. Jaskirat")      # Veterinarian

my_zoo.add_staff(piyush)
my_zoo.add_staff(dr_jaskirat)


print("Simone Zoo Welcomes You\n")

print("Animal sounds:")
print(tommy.make_sound())
print(mithu.make_sound())
print(simba.make_sound())

print("\n Piyush's daily routine:")
print(piyush.feed_animal(tommy))
print(piyush.clean_enclosure(grassland))

print("\n Health treatment by Dr. Jaskirat:")
dr_jaskirat.treat_animal(mithu, "Wing got injured", "24-11-2025", "high", "Rest and bandage")
mithu.get_health_records()[0].show_record()

print("\nMoving mithu during under treatment")
try:
    rainforest.remove_animal(mithu)
except:
    print("Cannot move mithu because of under treatment")

print("\n Final Zoo Report:")
my_zoo.show_zoo_report()

print("\nReport has been Completed. Thank you")