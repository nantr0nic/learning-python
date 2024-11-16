# Refresher

"""
# number refresher stuff
squares = [value**2 for value in range(1, 11)]
print(squares)

for num in range(1,21):
    print(num)

mil = range(1,1000001) # Doesn't work if mil is made a list []
print(sum(mil))
print(min(mil))
print(max(mil))

for num in range(1,21,2): print(num)
for num in range(3,31): print(num*3)

cubes = [value**3 for value in range(1,11)]
print (cubes)
"""

"""
# tuples
tuple = (1, 2, 3, 'hello', 'goodbye')
print(tuple[0])
print(tuple[0] + tuple[2])
print(tuple[3])

tuple = (4, 6, 8)
print(tuple[0])
print(tuple[0] + tuple[2])
"""

numbers = range(1, 101)

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
