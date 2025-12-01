# Defining Attributes and Methods for the Child Class

# Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

# Let’s add an attribute that’s specific to electric cars (a battery, for example) and a method to report on this attribute. 

# We’ll store the battery size and write a method that prints a description of the battery:


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75 #1

    def describe_battery(self): #2
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# At 1 we add a new attribute self.battery_size and set its initial value to, say, 75. 

# This attribute will be associated with all instances created from the ElectricCar class but won’t be associated with any instances of Car. 

# We also add a method called describe_battery() that prints information about the battery at 2.

# When we call this method, we get a description that is clearly specific to an electric car:

# There’s no limit to how much you can specialize the ElectricCar class. 

# You can add as many attributes and methods as you need to model an electric car to whatever degree of accuracy you need. 

# An attribute or method that could belong to any car, rather than one that’s specific to an electric car, should be added to the Car class instead of the ElectricCar class. 

# Then anyone who uses the Car class will have that functionality available as well, and the ElectricCar class will only contain code for the information and behavior specific to electric vehicles.
