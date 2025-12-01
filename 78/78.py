# Testing Multiple Conditions

# The if-elif-else chain is appropriate when you just need one test to pass. As soon as Python finds
# one test that passes, it skips the rest of the tests. This behaviour is beneficial, because it's
# efficient and allows you to test for one specific condition.

# Sometimes, it's important to check all the conditions of interest. In this case, you should use
# a series of simple if statements with no elif or else blocks. This technique makes sense when more
# than one condition could be True, and you want to act on every condition that is True.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# The three independent tests above are executed every time the program is run. Because every
# condition in the example is evaluated, both mushrooms and extra cheese are added to the pizza
