# Using Multiple elif Blocks
# You can use as many elif blocks in your code as you like
# Let's say anyone 65 or older pays half the regular admission

age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: # to check whether the person is less than age 65 before assigning them the full admission rate of $40
    price = 40
else:
    price = 20 # change from 40 to 20 as the only ages that make to this block are people 65 or older

print(f"Your admission cost is ${price}.")
