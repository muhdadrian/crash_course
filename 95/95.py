# Using get() to Access Values

# Using keys in square brackets to retrieve the value you're interested in from a dictionary might
# cause one potential problem: if the key you ask for doesn't exist, you'll get an error.
#
# Let's see what happens when you ask for the point value of an alien that doesn't have a point value
# set:

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

# The code above will output an error