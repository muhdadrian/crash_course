# Using the range() Function:
# Python's range() function makes it easy to generate a series of numbers.

for value in range(1, 5):
    print(value)

# it doesn't print the number 5

print('----------')


# To print the numbers from 1 to 5, you would use range(1, 6):

for value in range(1, 6):
    print(value)

print('----------')

# You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example,
# range(6) would return the numbers from 0 through 5.

for value in range(6):
    print(value)