# Making an Argument Optional

# Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. 

# You can use default values to make an argument optional.

# For example, say we want to expand get_formatted_name() to handle middle names as well. 

# A first attempt to include middle names might look like this:

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# This function works when given a first, middle, and last name. 

# The function takes in all three parts of a name and then builds a string out of them. 

# The function adds spaces where appropriate and converts the full name to title case: