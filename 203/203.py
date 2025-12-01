# Handling the FileNotFoundError Exception

# One common issue when working with files is handling missing files. The file you’re looking for might be in a different location, the filename may be misspelled, or the file may not exist at all. 

# You can handle all of these situations in a straightforward way with a try-except block.

# Let’s try to read a file that doesn’t exist. The following program tries to read in the contents of Alice in Wonderland, but I haven’t saved the file alice.txt in the same directory as alice.py:

filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()


# There are two changes here. One is the use of the variable f to represent the file object, which is a common convention. 

# The second is the use of the encoding argument. This argument is needed when your system’s default encoding doesn’t match the encoding of the file that’s being read.

# Python can’t read from a missing file, so it raises an exception:

# The last line of the traceback reports a FileNotFoundError: this is the exception Python creates when it can’t find the file it’s trying to open.
