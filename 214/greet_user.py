# Now let’s write a new program that greets a user whose name has already been stored:

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f) #1
    print(f"Welcome back, {username}!") #2


# At #1 we use json.load() to read the information stored in username.json and assign it to the variable username. Now that we’ve recovered the username, we can welcome them back #2:

# Welcome back, Eric!
