from car import Car

my_new_car = Car('honda', 'civic', 2007)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 165000
my_new_car.read_odometer()