# Looping Through All the Keys in a Dictionary
# The keys() method is useful when you don't need to work with all of the values in a dictionary.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys(): #1
    print(name.title())

# The line at 1 tells Python to pull all the keys from the dictionary favorite_languages and assign
# them one at a time to the variable name. The output shows the names of everyone who took the poll.

# Looping through the keys is actually the default behaviour when looping through a dictionary, so
# this code would have exactly the same output if you wrote:


#for name in favorite_languages:

#rather than...

#for name in favorite_languages.keys():

# You can choose to use the keys() method explicitly if it makes your code easier to read, or you
# can omit it if you wish.
#
# You can access the value associated with any key you care about inside the loop by using the current
# key.

