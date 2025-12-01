# Now we can import from each module separately and create whatever kind of car we need:

from car import Car #1
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# At #1 we import Car from its module, and ElectricCar from its module. We then create one regular car and one electric car. Both kinds of cars are created correctly:

#     2019 Volkswagen Beetle
#     2019 Tesla Roadster
