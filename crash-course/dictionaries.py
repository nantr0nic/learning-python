# DICTIONARY TIME!!! woo.

import os
import random
"""
os.system('cls')
print("beginning\n\n\n")
dict_0 = {
    'name': 'Andy',
    'age': 33,
    'height': 'tall'
}
# del <-- removes / ex: del dict_0['name']
for poop, v in dict_0.items():
    print(f"{v} is {poop}")

dict_1 = {}
# This vvv is wrong -- it only makes one key labeled 'num'
# for num in range(1,6): dict_1['num'] = random.random()

for num in range(1,6): dict_1[num] = random.random()
for name in dict_1.keys(): print(name)
for value in dict_1.values(): print(value)

# using dictionary comprehension:
dict_1 = {i: random.random() for i in range(1, 6)}

# for name in dict_1.keys(): print(name)
for poop in dict_1: print(poop) # <-- .keys() is optional, default behavior returns keys
for value in dict_1.values(): print(value)

for crap in dict_1: 
    if crap % 2 == 0: print(crap) # only even keys

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title() + ", thank you for taking the poll.")


### items() returns key/value pair 
### keys() returns key (but is optional...)
### values() returns values

Example code vvv
def transform_values(d):
    # Transform dictionary values by converting strings to uppercase.
    return {key: value.upper() for key, value in d.items()}

# Create a sample dictionary
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Apply the transformation using items()
transformed_data = transform_values(data)

print(transformed_data)
             ^^^


# Nesting a dictionary in a list

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

# Nesting a list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']: print("\t" + topping)

"""

# Nesting a dictionary in  a dictionary

users = {
    'Andy': {
        'height': 'tall',
        'age': 33,
    },
    'Heather': {
        'height': 'short',
        'age': 40,
    },
}

for name, info in users.items():
    print(f"Name: {name}")
    print(f"Height: {info['height']}")
    print(f"Age: {str(info['age'])}")