# Sorting a List Temporarily with the sorted() Function
# The sorted() function lets you display your list in a particular order but doesn't affect the
# actual order of the list.


cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.