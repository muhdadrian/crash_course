# Here’s what it looks like to import the entire car module and then create a regular car and an electric car:

import car #1

my_beetle = car.Car('volkswagen', 'beetle', 2019) #2
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019) #3
print(my_tesla.get_descriptive_name())


# At #1 we import the entire car module. We then access the classes we need through the module_name.

# ClassName syntax. At #2 we again create a Volkswagen Beetle, and at #3 we create a Tesla Roadster.
