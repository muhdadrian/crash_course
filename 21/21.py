# The append() method makes it easy to build lists dynamically
# For example, you can start with empty list and then add items to the list using a series of append() calls
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Building lists like above is very common, because you often won't know the data your users want to
# store in a program until after the program is running.
# To put your users in control, start by defining an empty list that will hold the users' values.
# Then append each new value provided to the list you just created.

