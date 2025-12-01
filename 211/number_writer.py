# Using json.dump() and json.load()

# Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. 

# The first program will use json.dump() to store the set of numbers, and the second program will use json.load().

# The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data. Here’s how you can use json.dump() to store a list of numbers:

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json' #1
with open(filename, 'w') as f: #2
    json.dump(numbers, f) #3


# when we run this program, it will create 'numbers.json' file

# We first import the json module and then create a list of numbers to work with. 

# At #1 we choose a filename in which to store the list of numbers. It’s customary to use the file extension .json to indicate that the data in the file is stored in the JSON format. 

# Then we open the file in write mode, which allows json to write the data to the file #2. 

# At #3 we use the json.dump() function to store the list numbers in the file numbers.json.

# This program has no output, but let’s open the file numbers.json and look at it. The data is stored in a format that looks just like Python:
