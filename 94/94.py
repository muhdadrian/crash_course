# A Dictionary of Similar Objects

# You can use a dictionary to store one kind of information about many objects. For example, say you
# want to poll a number of people and ask them what their favorite programming language is.


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title() #1
print(f"Sarah's favorite language is {language}")

# To see which language Sarah chose, we ask for the value at:
# favorite_languages['sarah']

# We use the syntax to pull Sarah's favorite language from the dictionary at 1 and assign it to the
# variable language. Creating a new variable here makes for a much cleaner print() call.
