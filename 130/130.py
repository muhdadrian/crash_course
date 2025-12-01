# Filling a Dictionary with User Input

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ") #1
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response #2

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ") #3_variables
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items(): #4
    print(f"{name} would like to climb {response}.")

# The program first defines an empty dictionary (responses) and sets a flag (polling_active) to indicate that polling is active. 

# As long as polling_active is True, Python will run the code in the while loop. 

# Within the loop, the user is prompted to enter their name and a mountain they’d like to climb at 1. 

# That information is stored in the responses dictionary at 2, and the user is asked whether or not to keep the poll running at 3. 

# If they enter yes, the program enters the while loop again. 

# If they enter no, the polling_active flag is set to False, the while loop stops running, and the final code block at 4 displays the results of the poll.

# To understand the code above where the answer is printed in dictionary:

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
    
#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ") 
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(responses)


# Simpler Version:

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
#     break

# print(responses)


# My answer in my restudy:

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response

#     user = input("Would you like to let another person respond? (yes/ no) ")
#     if user == 'no':
#         polling_active = False
#     else:
#         continue

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}") 

