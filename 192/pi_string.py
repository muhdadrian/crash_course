# The variable pi_string contains the whitespace that was on the left side of the digits in each line, but we can get rid of that by using strip() instead of rstrip():

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# Now we have a string containing pi to 30 decimal places. The string is 32 characters long because it also includes the leading 3 and a decimal point:

# When Python reads from a text file, it interprets all text in the file as a string. 

# If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.
