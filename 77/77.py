# Omitting the else Block:
# Python does not require an else block at the end of an if-elif chain. Sometimes an else block is
# useful;sometimes it is clearer to use an additional elif statement that catches the specific
# condition of interest:

age = 64

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:# this assigns a price of $20 when the person is 65 or older, which is a bit clearer than the general else block.
    price = 20

print(f"Your admission cost is ${price}.")

# The else block is a catchall statement. It matches any condition that wasn't matched by a specific
# if or elif test, and that can sometimes include invalid or even malicious data. If you have a
# specific final condition you are testing for, consider using a final elif block and omit the else
# block. As a result, you'll gain extra confidence that your code will run only under the correct
# conditions.
