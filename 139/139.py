def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# To describe an animal other than a dog, you could use a function call like this:

describe_pet(pet_name='harry', animal_type='hamster')

# Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.

# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. 

# This allows Python to continue interpreting positional arguments correctly.
