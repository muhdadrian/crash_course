with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# The only difference between this output and the original file is the extra blank line at the end of the output. 

# The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. 

# If you want to remove the extra blank line, you can use rstrip() in the call to print():

# Recall that Python’s rstrip() method removes, or strips, any whitespace characters from the right side of a string. Now the output matches the contents of the original file exactly:
