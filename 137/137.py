# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Note that the order of the parameters in the function definition had to be changed. 

# Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet’s name. 

# Python still interprets this as a positional argument, so if the function is called with just a pet’s name, that argument will match up with the first parameter listed in the function’s definition. 

# This is the reason the first parameter needs to be pet_name.
