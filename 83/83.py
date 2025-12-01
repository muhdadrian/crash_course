# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']#1

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']#2

for requested_topping in requested_toppings:#3
    if requested_topping in available_toppings:#4
        print(f"Adding {requested_topping}.")
    else:#5
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# 1 - we define a list. This could be a tuple if the pizzeria has a stable selection of toppings.
# 2 - we make a list of toppings that a customer has requested.
# 3 - we loop through the list of requested toppings. Inside the loop, we first check if each
# requested topping is in the list of available_toppings in 4.
# 4 - we add the topping to the pizza if there's in the list.
# 5 - If the requested_topping is not in the list of available_toppings, the else block will run.

# The code syntax above produces clean, informative output.
# In just a few lines of code, we've managed a real-world situation pretty effectively!