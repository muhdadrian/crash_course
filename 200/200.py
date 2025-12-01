# Using try-except Blocks

# When you think an error may occur, you can write a try-except block to handle the exception that might be raised. 

# You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception.

# Here’s what a try-except block for handling the ZeroDivisionError exception looks like:


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block. 

# If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.

# In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. Python then runs the code in that block, and the user sees a friendly error message instead of a traceback:

# You can't divide by zero!

# If more code followed the try-except block, the program would continue running because we told Python how to handle the error. 

# Let’s look at an example where catching an error can allow a program to continue running.
