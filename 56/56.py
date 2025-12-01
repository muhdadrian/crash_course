# Writing over a Tuple
# - although you can't modify tuple, you can assign a new value to a variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple:

dimensions = (200, 50)# we define the original tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)# we associate a new tuple with the variable dimensions
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# reassigning a variable is valid

# When compared with lists, tuples are simple data structures. Use them when you want to store a set
# of values that should not be changed throughout the life of a program.
 
