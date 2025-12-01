# Including newlines in your calls to write() makes each string appear on its own line:


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# The output now appears on separate lines:

# I love programming.
# I love creating new games.

# You can also use spaces, tab characters, and blank lines to format your output, just as you’ve been doing with terminal-based output.
