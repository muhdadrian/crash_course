# Tuples:
# - immutable list.
# - it uses parentheses instead of brackets (brackets for list).
# - example - we have a rectangle that should always be a certain size, we can ensure that its size
# doesn't change by putting the dimensions into a tuple:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Let's see what happens if we try to change one of the items in the tuple dimensions:
dimensions[0] = 250 # this will output error, as we can't change tuple

# - Tuples are technically defined by the presence of a comma; the parentheses make them look neater
# and more readable. If you want to define a tuple with one element, you need to include a trailing
# comma:
# - It doesn't often make sense to build a tuple with one element, but this can happen when tuples are
# generated automatically.

my_t = (3,)
