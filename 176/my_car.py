# we make a separate file called my_car.py. This file will import the Car class and then create an instance from that class:

from car import Car #1

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# The import statement at #1 tells Python to open the car module and import the class Car. 

# Now we can use the Car class as if it were defined in this file. The output is the same as we saw earlier:

# 2019 Audi A4
# This car has 23 miles on it.

# Importing classes is an effective way to program. Picture how long this program file would be if the entire Car class were included. 

# When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program file clean and easy to read. 

# You also store most of the logic in separate files; once your classes work as you want them to, you can leave those files alone and focus on the higher-level logic of your main program.
