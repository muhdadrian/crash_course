# Working with a File’s Contents

# After you’ve read a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits of pi. 

# First, we’ll attempt to build a single string containing all the digits in the file with no whitespace in it:


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' #1
for line in lines: #2
    pi_string += line.rstrip()

print(pi_string) #3
print(len(pi_string))


# We start by opening the file and storing each line of digits in a list, just as we did in the previous example. 

# At #1 we create a variable, pi_string, to hold the digits of pi. We then create a loop that adds each line of digits to pi_string and removes the newline character from each line #2 

# At #3 we print this string and also show how long the string is:
