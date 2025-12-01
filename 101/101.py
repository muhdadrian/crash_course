# You can also use the keys() method to find out if a particular person was polled:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys(): #1
    print(f"Erin, please take our poll!")


# The keys() method isn't just for looping: it actually returns a list of all the keys, and the line

# at 1 simply checks if 'erin' is in this list. Because she's not, a message is printed inviting her to take the poll. 


