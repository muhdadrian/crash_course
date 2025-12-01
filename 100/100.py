favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah'] #1
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends: #2
        language = favorite_languages[name].title() #3
        print(f"\t{name.title()}, I see you love {language}!")

# 1 - we make a list of friends that we want to print a message to. Inside the loop, we print each
# person's name.
# 2 - we check whether the name we're working with is in the list friends. If it is, we determine
# the person's favorite language using the name of the dictionary and the current value of name as
# they key at 3. We then print a special greeting, including a reference to their language of choice.
#
# Everyone's name is printed, but our friends receive a special message.

# To understand the problem above:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# language = favorite_languages['sarah'].title()
# print(language)
