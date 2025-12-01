# The Modulo Operator:

# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

# The modulo operator tells you what the remainder is. 

# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. 

# You can use this fact to determine if a number is even or odd:

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

