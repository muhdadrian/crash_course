# Removing Elements from a List:
# when a user decides to cancel their account on a web application you created, you'll want to
# remove that user from the list of active users. You can remove an item according to its position
# in the list or according to its value


# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can use the del
# statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# del motorcycles[0] # remove 1st item
# print(motorcycles)

del motorcycles[1] # remove 2nd item
print(motorcycles)

# In both examples above, you can no longer access the value that was removed from the list after
# the del statement is used.