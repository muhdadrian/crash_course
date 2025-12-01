# Returning a Dictionary

# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. 

# For example, the following function takes in parts of a name and returns a dictionary representing a person:

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# The function build_person() takes in a first and last name, and puts these values into a dictionary at 1. 

# The value of first_name is stored with the key 'first', and the value of last_name is stored 
# with the key 'last'. 

# The entire dictionary representing the person is returned at 2. 

# The return value is printed at 3 with the original two pieces of textual information now stored in a dictionary:

# This function takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it. 

# The strings 'jimi' and 'hendrix' are now labeled as a first name and last name. 

# You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person. 

# For example, the following change in 145.py allows you to store a person’s age as well
