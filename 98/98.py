# Because the keys always refer to a person's name and the value is always a language,
# we'll use the variables name and language in the loop instead of key and value. This will make
# it easier to follow what's happening inside the loop:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items(): #1
    print(f"{name.title()}'s favorite language is {language.title()}.") #2

# The code at 1 tells Python to loop through each key-value pair in the dictionary. As it works
# through each pair the key is assigned to the variable name, and the value is assigned to the
# variable language. These descriptive names make it much easier to see what the print() call at 2 is doing.

# This type of looping would work just as well if our dictionary stored the results from polling a
# thousand or even a million people.
