# We should factor one more block of code out of greet_user(). If the username doesn’t exist, we should move the code that prompts for a new username to a function dedicated to that purpose:

import json
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()


# Each function in this final version of remember_me.py has a single, clear purpose. We call greet_user(), and that function prints an appropriate message: it either welcomes back an existing user or greets a new user. It does this by calling get_stored_username(), which is responsible only for retrieving a stored username if one exists. 

# Finally, greet_user() calls get_new_username() if necessary, which is responsible only for getting a new username and storing it. 

# This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend.
