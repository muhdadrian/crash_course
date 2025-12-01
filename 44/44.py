# List Comprehensions:
# a list comprehensions allows you to generate list in a line of code,
# it combines the for loop and the creation of new elements into one line, and automatically appends each new element.

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# - begin with descriptive name for the list, such as squares.
# - open a set of square brackets and define the expression for the values you want to store in the
# new list
# - the expression is value**2, which raises the value to the second power
# - then, write a for loop to generate the numbers you want to feed into the expression, and close the
# square brackets.
# - the for loop is for value in range(1, 11), which feeds the values 1 through 10 into the expression
# value**2.
# - no colon is used at the end of the for statement.

# It takes practice to write your own list comprehensions