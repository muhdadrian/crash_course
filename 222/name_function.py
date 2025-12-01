# A Failing Test

# What does a failing test look like? Let’s modify get_formatted_name() so it can handle middle names, but we’ll do so in a way that breaks the function for names with just a first and last name, like 

# Janis Joplin.

# Here’s a new version of get_formatted_name() that requires a middle name argument:

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# This version should work for people with middle names, but when we test it, we see that we’ve broken the function for people with just a first and last name. 
