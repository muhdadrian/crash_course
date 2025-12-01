# Now we’ll write a program that uses json.load() to read the list back into memory:

import json

filename = 'numbers.json' #1
with open(filename) as f: #2
    numbers = json.load(f) #3

print(numbers)


# At #1 we make sure to read from the same file we wrote to. This time when we open the file, we open it in read mode because Python only needs to read from the file #2. 

# At #3 we use the json.load() function to load the information stored in numbers.json, and we assign it to the variable numbers. 

# Finally we print the recovered list of numbers and see that it’s the same list created in number_writer.py:

# [2, 3, 5, 7, 11, 13]

# This is a simple way to share data between two programs.
