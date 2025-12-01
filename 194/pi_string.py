#Is Your Birthday Contained in Pi?

# I’ve always been curious to know if my birthday appears anywhere in the digits of pi. Let’s use the program we just wrote to find out if someone’s birthday appears anywhere in the first million digits of pi. 

# We can do this by expressing each birthday as a string of digits and seeing if that string appears anywhere in pi_string:

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ") #1
if birthday in pi_string: #2
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# At #1 we prompt for the user’s birthday, and then at #2 we check if that string is in pi_string.
 
# Let’s try it:

# Enter your birthdate, in the form mmddyy: 120372
# Your birthday appears in the first million digits of pi!

# My birthday does appear in the digits of pi! Once you’ve read from a file, you can analyze its contents in just about any way you can imagine.



