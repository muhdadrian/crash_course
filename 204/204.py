# In this example, the open() function produces the error, so to handle it, the try block will begin with the line that contains open():

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# In this example, the code in the try block produces a FileNotFoundError, so Python looks for an except block that matches that error. Python then runs the code in that block, and the result is a friendly error message instead of a traceback:
