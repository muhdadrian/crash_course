# Using range() to Make a List of Numbers

numbers = list(range(1, 6))
print(numbers)

print('----------')

# We can also use the range() function to tell Python to skip numbers in a given range. If you pass a
# third argument to range(), Python uses that value as a step size when generating numbers. For
# example, here's how to list the even numbers between 1 and 10:

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# The range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly
# until it reaches or passes the end value, 11.
