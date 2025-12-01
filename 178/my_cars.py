from car import Car, ElectricCar #1

my_beetle = Car('volkswagen', 'beetle', 2019) #2
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019) #3
print(my_tesla.get_descriptive_name())


# You import multiple classes from a module by separating each class with a comma #1. 

# Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.

# In this example we make a regular Volkswagen Beetle at #2 and an electric Tesla Roadster at #3:

#    2019 Volkswagen Beetle
#    2019 Tesla Roadster


