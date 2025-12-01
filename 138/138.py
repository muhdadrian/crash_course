def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# The simplest way to use this function now is to provide just a dog’s name in the function call:

describe_pet('willie')

# This function call would have the same output as the previous example. 

# The only argument provided is 'willie', so it is matched up with the first parameter in the definition, pet_name. 

# Because no argument is provided for animal_type, Python uses the default value 'dog'.
