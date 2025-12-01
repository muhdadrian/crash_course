# Now we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The function responds appropriately, whether it receives one value or three values.

# This syntax works no matter how many arguments the function receives.