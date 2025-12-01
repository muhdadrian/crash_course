# Importing an Entire Module

# To start importing functions, we first need to create a module. 

# A module is a file ending in .py that contains the code you want to import into your program. Let’s make a module that contains the function make_pizza().


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Now we’ll make a separate file called making_pizza.py in the same directory as pizza.py. 

# This file imports the module we just created and then makes two calls to make_pizza():

