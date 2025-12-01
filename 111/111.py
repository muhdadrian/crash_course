# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.

favorite_languages = { #1
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items(): #2
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: #3
        print(f"\t{language.title()}")


#1 - the value associated with each name is now a list. Notice that some people have one favorite language and others have multiple favorites. 

# When we loop through the dictionary at 2, we use the variable name languages to hold each value from the dictionary, because we know that each value will be a list. 

# Inside the main dictionary loop, we use another for loop at 3 to run through each person's list of favorite languages. 

# we can refine the code at 112.py