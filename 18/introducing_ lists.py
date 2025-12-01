# Lists are one of Python's most powerful features readily accessible to new programmers.
# A list is a collection of items in a particular order.
# A list usually contains more than one element, it's a good idea to make the name of your list
# plural, such as letters, digits, or names
# In Python, square brackets ([]) indicate a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # The output is not what you want your users to see

# Accessing Elements in a List
# Lists are ordered collections, so you can access any element in a list by telling Python the
# position, or index, of the item desired.


print(bicycles[0]) #This is the result you want your users to see - clean, neatly formatted output.

# You can format the element 'trek' more neatly by using title() method where Trek is capitalized.
print(bicycles[0].title())

# index 1 and 3
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list by asking for the item at index -1.
print(bicycles[-1])

# This syntax is quite useful, because you want to access the last items in a list without knowing
# exactly how long the list is.
# While, the index -2 returns the second item from the end of the list
# The index -3 returns the third item from the end, and so forth
