# Writing Multiple Lines

# The write() function doesn’t add any newlines to the text you write. So if you write more than one line without including newline characters, your file may not look the way you want it to:

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# If you open programming.txt, you’ll see the two lines squished together:

# I love programming.I love creating new games.
