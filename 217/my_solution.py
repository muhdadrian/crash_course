import json

filename = 'username.json' # I put this variable in global var when the greet_user() is not working. It's still working.

# I found out that it's repetitive to use filename twice in remember_me.py

def get_stored_username():
    """get stored username"""
    
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """greet user"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")    
    else:
        username = input("What is your name? ")
        with open(filename , 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

greet_user()