# Indenting Unnecessarily After the Loop

# If you accidentally, indent code that should run after a loop has finished, that code will be repeated
# once for each item in the list. Often, this will result in a logical error.


students = ['sarah', 'fatih', 'fariq']
for student in students:
    print(f"{student.title()}, you're brilliant!")
    print(f"I can't wait to see you next result, {student.title()}.\n")

    print("Thank you, everyone. That was a great achievement!")# because this line is indented, it's printed once for each person in the list