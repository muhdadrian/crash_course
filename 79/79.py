# The code below would not work properly if we used an if-elif-else block, because the code would
# stop running after only one test passes:

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# The test for 'mushrooms' is the first test to pass, so mushrooms are added to the pizza. However,
# the values 'extra cheese' and 'pepperoni' are never checked, because Python doesn't run any tests
# beyond the first test that passes in an if-elif-else chain. The customer's first topping will be
# added, but all of their other toppings will be missed.

# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one
# block of code needs to run, use a series of independent if statements.
