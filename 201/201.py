# Using Exceptions to Prevent Crashes

# Handling errors correctly is especially important when the program has more work to do after the error occurs. 

# This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing.

# Let’s create a simple calculator that does only division:


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)


# This program does nothing to handle errors, so asking it to divide by zero causes it to crash:
