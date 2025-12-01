# These blank lines appear because an invisible newline character is at the end of each line in the text file. 

# The print function adds its own new line each time we call it, so we end up with two newline characters at the end of each line: one from the file and one from print(). Using rstrip() on each line in the print() call eliminates these extra blank lines:


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Now the output matches the contents of the file once again:


