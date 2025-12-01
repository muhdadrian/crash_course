# Styling Functions


# You need to keep a few details in mind when you’re styling functions. Functions should have descriptive names, and these names should use lowercase letters and underscores. 

# Descriptive names help you and others understand what your code is trying to do. 

# Module names should use these conventions as well.

# Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format. 

# In a well-documented function, other programmers can use the function by reading only the description in the docstring. 

# They should be able to trust that the code works as described, and as long as they know the name of the function, the arguments it needs, and the kind of value it returns, they should be able to use it in their programs.

# If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:

# def function_name(parameter_0, parameter_1='default value')


# The same convention should be used for keyword arguments in function calls:

# function_name(value_0, parameter_1='value')


# PEP 8 (https://www.python.org/dev/peps/pep-0008/) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window. 

# If a set of parameters causes a function’s definition to be longer than 79 characters, press enter after the opening parenthesis on the definition line.

# On the next line, press TaB twice to separate the list of arguments from the body of the function, which will only be indented one level.

# Most editors automatically line up any additional lines of parameters to match the indentation you have established on the first line:

# def function_name(
#         parameter_0, parameter_1, parameter_2, 
#         parameter_3, parameter_4, parameter_5):
#     function body...


# If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.

# All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.


# One of your goals as a programmer should be to write simple code that does what you want it to, and functions help you do this. 

# They allow you to write blocks of code and leave them alone once you know they work. 

# When you know a function does its job correctly, you can trust that it will continue to work and move on to your next coding task.


# Classes combine functions and data into one neat package that can be used in flexible and efficient ways.
