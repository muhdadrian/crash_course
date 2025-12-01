# The revised code below is easier to modify than the original approach. To change the text
# of the output message, you would need to change only one print() call rather than three
# separate print() calls.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
