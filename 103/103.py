# Looping Through All Values in a Dictionary
# You can use values() method to return a list of values without any keys

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# The for statement here pulls each value from the dictionary and assigns it to the variable language.