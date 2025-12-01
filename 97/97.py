# Looping Through a Dictionary
# Looping Through All Key-Value Pairs

user_0 = {
    'username': 'adriannandu',
    'first': 'adrian',
    'last': 'nandu',
}

for key, value in user_0.items(): #1
    print(f"\nKey: {key}") #2
    print(f"Value: {value}") #3

"""
1 - to write a for loop for a dictionary, you create names for the two variables that will hold the
key and value in each key-value pair. You can choose any names you want for these two variables.
This code would work just as well if you had used abbreviations for the variable names, like below: 
"""

# for k, v in user_0.items()

# 1 - in the second half, it includes the name of the dictionary followed by the method items(), which
# returns a list of key-value pairs. The for loop then assigns each of these pairs to the two
# variables provided. In the preceding example, we use the variables to print each key at 2, followed
# by associated value at 3.
#
# The "\n" in the first print() call ensures that a blank line is inserted before each key-value pair
# in the output.
