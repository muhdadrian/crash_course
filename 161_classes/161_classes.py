# Creating the Dog Class

# Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():


class Dog: #1
    """A simple attempt to model a dog.""" #2

    def __init__(self, name, age): #3
        """Initialize name and age attributes."""
        self.name = name #4
        self.age = age

    def sit(self): #5
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# There’s a lot to notice here, but don’t worry. 

# You’ll see this structure throughout this chapter and have lots of time to get used to it. 

# At 1 we define a class called Dog. By convention, capitalized names refer to classes in Python. There are no parentheses in the class definition because we’re creating this class from scratch. 

# At 2 we write a docstring describing what this class does.

# The __init__() Method

# A function that’s part of a class is a method. 

# Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call methods. 

# The __init__() method at 3 is a special method that Python runs automatically whenever we create a new instance based on the Dog class. 

# This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names. 

# Make sure to use two underscores on each side of __init__(). 

# If you use just one on each side, the method won’t be called automatically when you use your class, which can result in errors that are difficult to identify.

# We define the __init__() method to have three parameters: self, name, and age. The self parameter is required in the method definition, and it must come first before the other parameters. 

# It must be included in the definition because when Python calls this method later (to create an instance of Dog), the method call will automatically pass the self argument. 

# Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class. 

# When we make an instance of Dog, Python will call the __init__() method from the Dog class. 

# We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it. 

# Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.

# The two variables defined at 4 each have the prefix self. 

# Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class. 

# The line self.name = name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created. 

# The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.

# The Dog class has two other methods defined: sit() and roll_over() at 5. 

# Because these methods don’t need additional information to run, we just define them to have one parameter, self. 

# The instances we create later will have access to these methods. 

# In other words, they’ll be able to sit and roll over. For now, sit() and roll_over() don’t do much. 

# They simply print a message saying the dog is sitting or rolling over. 

# But the concept can be extended to realistic situations: if this class were part of an actual computer game, these methods would contain code to make an animated dog sit and roll over. 

# If this class was written to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.

