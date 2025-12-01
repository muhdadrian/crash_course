# Saving and Reading User-Generated Data

# Saving data with json is useful when you’re working with user-generated data, because if you don’t store your user’s information somehow, you’ll lose it when the program stops running. 

# Let’s look at an example where we prompt the user for their name the first time they run a program and then remember their name when they run the program again.

# Let’s start by storing the user’s name:

import json

username = input("What is your name? ") #1

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f) #2
    print(f"We'll remember you when you come back, {username}!") #3


# At #1 we prompt for a username to store. Next, we use json.dump(), passing it a username and a file object, to store the username in a file #2. Then we print a message informing the user that we’ve stored their information #3:

# What is your name? Eric
# We'll remember you when you come back, Eric!
