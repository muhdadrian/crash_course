# Working with Classes and Instances
# The Car Class

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): #1
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self): #2
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019) #3
print(my_new_car.get_descriptive_name())


# At 1 in the Car class, we define the __init__() method with the self parameter first, just like we did before with our Dog class. We also give it three other parameters: make, model, and year. 

# The __init__() method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class. 

# When we make a new Car instance, we’ll need to specify a make, model, and year for our instance.

# At 2 we define a method called get_descriptive_name() that puts a car’s year, make, and model into one string neatly describing the car. 

# This will spare us from having to print each attribute’s value individually. 

# To work with the attribute values in this method, we use self.make, self.model, and self.year. 

# At 3 we make an instance from the Car class and assign it to the variable my_new_car. Then we call get_descriptive_name() to show what kind of car we have:
