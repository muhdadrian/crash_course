# Using Arbitrary Keyword Arguments


# Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. 

# In this case, you can write functions that accept as many key-value pairs as the calling statement provides. 

# One example involves building user profiles: you know you’ll get information about a user, but you’re not sure what kind of information you’ll receive. 

# The function build_profile() in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first #1
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. 

# The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. 

# Within the function, you can access the key- value pairs in user_info just as you would for any dictionary.

# In the body of build_profile(), we add the first and last names to the user_info dictionary because we’ll always receive these two pieces of information from the user at 1, and they haven’t been placed into the dictionary yet. 

# Then we return the user_info dictionary to the function call line.

# We call build_profile(), passing it the first name 'albert', the last name 'einstein', and the two key-value pairs location='princeton' and field='physics'. 

# We assign the returned profile to user_profile and print user_profile.

# The returned dictionary contains the user’s first and last names and, in this case, the location and field of study as well. 

# The function would work no matter how many additional key-value pairs are provided in the function call.

# You can mix positional, keyword, and arbitrary values in many different ways when writing your own functions. 

# It’s useful to know that all these argument types exist because you’ll see them often when you start reading other people’s code. 

# It takes practice to learn to use the different types correctly and to know when to use each type. 

# For now, remember to use the simplest approach that gets the job done. As you progress you’ll learn to use the most efficient approach each time.

# You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments.
