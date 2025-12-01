# Mixing Positional and Arbitrary Arguments

# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. 

# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

# For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter *toppings:


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# In the function definition, Python assigns the first value it receives to the parameter size. 

# All other values that come after are stored in the tuple toppings. The function calls include an argument for the size first, followed by as many toppings as needed.

# Now each pizza has a size and a number of toppings, and each piece of information is printed in the proper place, showing size first and toppings after:

# You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
