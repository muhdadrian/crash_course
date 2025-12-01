# Incrementing an Attribute’s Value Through a Method

# Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value. 

# Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. 

# Here’s a method that allows us to pass this incremental amount and add that value to the odometer reading:


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): #1
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015) #2
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) #3
my_used_car.read_odometer()

my_used_car.increment_odometer(100) #4
my_used_car.read_odometer()


# The new method increment_odometer() at 1 takes in a number of miles, and adds this value to self.odometer_reading. 

# At 2 we create a used car, my_used_car. We set its odometer to 23,500 by calling update_odometer() and passing it 23_500 at 3. 

# At 4 we call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it:

# You can easily modify this method to reject negative increments so no one uses this function to roll back an odometer.

# You can use methods like this to control how users of your program update values such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. 

# Effective security takes extreme attention to detail in addition to basic checks like those shown here.
