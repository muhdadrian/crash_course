# But middle names aren’t always needed, and this function as written would not work if you tried to call it with only a first name and a last name. 

# To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value.

# To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty string and move it to the end of the list of parameters:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# In this example, the name is built from three possible parts. 

# Because there’s always a first and last name, these parameters are listed first in the function’s definition. 

# The middle name is optional, so it’s listed last in the definition, and its default value is an empty string at 1.

# In the body of the function, we check to see if a middle name has been provided. Python interprets non-empty strings as True, so if middle_name evaluates to True if a middle name argument is in the function call at 2. 

# If a middle name is provided, the first, middle, and last names are combined to form a full name. 

# This name is then changed to title case and returned to the function call line where it’s assigned to the variable musician and printed. 

# If no middle name is provided, the empty string fails the if test and the else block runs at 3. 

# The full name is made with just a first and last name, and the formatted name is returned to the calling line where it’s assigned to musician and printed.

# Calling this function with a first and last name is straightforward. If we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly at 4.

# This modified version of our function works for people with just a first and last name, and it works for people who have a middle name as well:

# Optional values allow functions to handle a wide range of use cases while letting function calls remain as simple as possible.
