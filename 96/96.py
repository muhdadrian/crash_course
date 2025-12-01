# You can use the get() method to set a default value that will be returned if the requested key
# doesn't exist.
#
# The get() method requires a key as a first argument. As a second optional argument, you can pass
# the value to be returned if the key doesn't exist:

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If the key 'points' exists in the dictionary, you'll get the corresponding value. If it doesn't,
# you get the default value. In this case, points doesn't exist, and we get a clean message instead
# of an error.
#
# If there's a chance the key you're asking for might not exist, consider using the get() method
# instead of the square bracket notation.
#
# If you leave out the second argument in the call to get() and the key doesn't exist, Python will
# return the value None. The special value None means 'no value exists'. This is not an error: it's
# a special value meant to indicate the absence of a value.

