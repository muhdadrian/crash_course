# The if-elif-else Chain

# Many real-world situations involve more than two possible conditions. For example, consider an
# amusement park that charges different rates for different age groups:

# - Admission for anyone under age 4 is free.
# - Admission for anyone between the ages of 4 and 18 is $25.
# - Admission for anyone age 18 or older is $40.

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# any age greater than 17 would cause the first two tests to fail - the else block would be executed.