import json
    
filename = 'username.json'

def get_stored_username():
    """get stored username"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def prompt_username():
    """get a username"""
    username = input("What is your name? ")
    with open(filename , 'w') as f:
        json.dump(username, f)
    return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """greet user"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = prompt_username()
        print(f"We'll remember you when you come back, {username}!")    

greet_user()




