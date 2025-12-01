# Looping Through a Dictionary's Keys in a Particular Order

# Starting in Python 3, looping through a dictionary returns the items in the same order they were inserted. 

# Sometimes, though, you'll want to loop through a dictionary in a different order.

# You can use the sorted() function to get a copy of the keys in order:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):#1
    print(f"{name.title()}, thank you for taking the poll.")

# 1 - This tells Python to list all keys in the dictionary and sort that list before looping through it.
