# We need to combine these two programs into one file. When someone runs remember_me.py, we want to retrieve their username from memory if possible; therefore, we’ll start with a try block that attempts to recover the username. 

# If the file username.json doesn’t exist, we’ll have the except block prompt for a username and store it in username.json for next time:

import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f: #1
        username = json.load(f) #2
except FileNotFoundError: #3
    username = input("What is your name? ") #4
    with open(filename, 'w') as f: #5
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
        print(f"Welcome back, {username}!")


# There’s no new code here; blocks of code from the last two examples are just combined into one file. 

# At #1 we try to open the file username.json. If this file exists, we read the username back into memory #2 and print a message welcoming back the user in the else block. 

# If this is the first time the user runs the program, username.json won’t exist and a FileNotFoundError will occur #3. 

# Python will move on to the except block where we prompt the user to enter their username #4. 

# We then use json.dump() to store the username and print a greeting #5.

# Whichever block executes, the result is a username and an appropriate greeting. If this is the first time the program runs, this is the output:

# What is your name? Eric
# We'll remember you when you come back, Eric!

# Otherwise:

# Welcome back, Eric!
   
# This is the output you see if the program was already run at least once.
