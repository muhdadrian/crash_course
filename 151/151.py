# Passing an Arbitrary Number of Arguments


# Python allows a function to collect an arbitrary number of arguments from the calling statement.

# For example, consider a function that builds a pizza. It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want. 

# The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple. 

# The print() call in the function body produces output showing that Python can handle a function call with one value and a call with three values. 

# It treats the different calls similarly. Note that Python packs the arguments into a tuple, even if the function receives only one value:

