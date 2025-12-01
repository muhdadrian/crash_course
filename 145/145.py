def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# We add a new optional parameter age to the function definition and assign the parameter the special value None, which is used when a variable has no specific value assigned to it. 

# You can think of None as a placeholder value. 

# In conditional tests, None evaluates to False. 

# If the function call includes a value for age, that value is stored in the dictionary. 

# This function always stores a person’s name, but it can also be modified to store any other information you want about a person.
