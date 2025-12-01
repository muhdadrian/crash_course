# Making an Instance from a Class


# Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.

# Let’s make an instance representing a specific dog:


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) #1

print(f"My dog's name is {my_dog.name}.") #2
print(f"My dog is {my_dog.age} years old.") #3


# The Dog class we’re using here is the one we just wrote in the previous example. 

# At 1 we tell Python to create a dog whose name is 'Willie' and whose age is 6. 

# When Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. 

# Python then returns an instance representing this dog. We assign that instance to the variable my_dog. 

# The naming convention is helpful here: we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.

# Accessing Attributes

# To access the attributes of an instance, you use dot notation. At 2 we access the value of my_dog’s attribute name by writing:

# my_dog.name

# Dot notation is used often in Python. This syntax demonstrates how Python finds an attribute’s value. 

# Here Python looks at the instance my_dog and then finds the attribute name associated with my_dog. 

# This is the same attribute referred to as self.name in the class Dog. At 3 we use the same approach to work with the attribute age.

# ChatGPT:
# {my_dog.name} is part of an f-string (formatted string literal) in Python. Here's a breakdown:

# What it means:
# my_dog is the object (or instance) of the Dog class you created.

# name is an attribute of that object (defined as self.name in the class).

# So my_dog.name accesses the value of the name attribute (in this case, 'Willie').
