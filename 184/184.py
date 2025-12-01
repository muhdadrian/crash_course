# Another useful function is choice(). This function takes in a list or tuple and returns a randomly chosen element:

from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)


# The random module shouldn’t be used when building security-related applications, but it’s good enough for many fun and interesting projects.

# You can also download modules from external sources. You’ll see a number of these examples in Part II, where we’ll need external modules to complete each project.
