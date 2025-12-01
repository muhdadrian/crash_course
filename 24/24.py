# Removing an Item Using the pop() method:
# - The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# - In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.
# - Another example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()# we pop a value from the list and store that value in the variable popped_motorcycle
print(motorcycles)# we print the list to show that a value has been removed from the list
print(popped_motorcycle)# then, we print the popped value to prove that we still have access to the value that was removed

# The output shows that the value 'suzuki' was removed from the end of the list and is now assigned to the variable popped_motorcycle

