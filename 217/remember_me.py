# Let’s refactor greet_user() so it’s not doing so many different tasks. We’ll start by moving the code for retrieving a stored username to a separate function:

import json
def get_stored_username():
    """Get stored username if available.""" #1
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None #2
    else:
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username: #3
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
           json.dump(username, f)
           print(f"We'll remember you when you come back, {username}!")

greet_user()


# The new function get_stored_username() has a clear purpose, as stated in the docstring at #1. 

# This function retrieves a stored username and returns the username if it finds one. 

# If the file username.json doesn’t exist, the function returns None #2. This is good practice: a function should either return the value you’re expecting, or it should return None. 

# This allows us to perform a simple test with the return value of the function. At #3 we print a welcome back message to the user if the attempt to retrieve a username was successful, and if it doesn’t, we prompt for a new username.

# We should factor one more block of code out of greet_user(). If the username doesn’t exist, we should move the code that prompts for a new username to a function dedicated to that purpose:

