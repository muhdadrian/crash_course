# Setting a Default Value for an Attribute


# When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the __init__() method, where they are assigned a default value.

# Let’s add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer:

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #1

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): #2
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example. 

# Then Python creates a new attribute called odometer_reading and sets its initial value to 0 at 1. We also have a new method called read_odometer() at 2 that makes it easy to read a car’s mileage.

# Our car starts with a mileage of 0: