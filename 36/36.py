# Doing More Work Within a for Loop

students = ['sarah', 'fatih', 'fariq']
for student in students:
    print(f"{student.title()}, you're brilliant!")

# Every indented line following the line for student in students is considered inside loop.
# Each indented line is executed once for each value in the list.
# Therefore, you can do as much work as you like with each value in the list.