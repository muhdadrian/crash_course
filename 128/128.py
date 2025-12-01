# Using a while Loop with Lists and Dictionaries

# A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list.

# To modify a list as you work through it, use a while loop.

# Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.


# Moving Items from One List to Another:

# Start with users that need to be verified,and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace'] #1
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users: #2
    current_user = unconfirmed_users.pop() #3

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) #4

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# We begin with a list of unconfirmed users at 1 (Alice, Brian, and Candace) and an empty list to hold confirmed users.

# The while loop at 2 runs as long as the list unconfirmed_users is not empty.

# Within this loop, the pop() function at 3 removes unverified users one at a time from the end of unconfirmed_users.

# Here, because Candace is last in the unconfirmed_users list, her name will be the first to be removed, assigned to current_user, and added to the confirmed_users list at 4.

# Next is Brian, then Alice.

# We simulate confirming each user by printing a verification message and then adding them to the list of confirmed users.

# As the list of unconfirmed users shrinks, the list of confirmed users grows.

# When the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed.
