"""
from car import Car, ElectricCar

my_honda = Car('honda', 'civic', 2007)
print(my_honda.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
"""

import car

my_honda = car.Car('honda', 'civic', 2007)
print(my_honda.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())