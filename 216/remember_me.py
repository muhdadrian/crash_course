# Refactoring

# Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. 

# This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

# We can refactor remember_me.py by moving the bulk of its logic into one or more functions. 

# The focus of remember_me.py is on greeting the user, so let’s move all of our existing code into a function called greet_user():


import json

def greet_user():
    """Greet the user by name.""" #1
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()

# Because we’re using a function now, we update the comments with a docstring that reflects how the program currently works #1. 

# This file is a little cleaner, but the function greet_user() is doing more than just greeting the user—it’s also retrieving a stored username if one exists and prompting for a new username if one doesn’t exist.

