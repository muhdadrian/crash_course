# Multiple Function Calls

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Calling a function multiple times is a very efficient way to work. 

# The code describing a pet is written once in the function. Then, anytime you want to describe a new pet, you call the function with the new pet’s information. 

# Even if the code for describing a pet were to expand to ten lines, you could still describe a new pet in just one line by calling the function again.
