# Using int() to Accept Numerical Input

# When you use the input() function, Python interprets everything the user enters as a string.

age = input("How old are you?")
print(age)

# The user enters the number 21 for example, but when we ask Python for the value of age, it returns '21', the string representation of the numerical value entered. 

# We know Python interpreted the input as a string because the number is now enclosed in quotes. 

# If all you want to do is print the input, this works well. But if you try to use the input as a number, you'll get an error:

print(age >= 18) # 1

# When you try to use the input to do a numerical comparison at 1, Python produces an error because it can’t compare a string to an integer: the string '21' that’s assigned to age can’t be compared to the numerical value 18.

# We can resolve this issue by using the int() function, which tells Python to treat the input as a numerical value. 

# The int() function converts a string representation of a number to a numerical representation. Go to 118.py.
