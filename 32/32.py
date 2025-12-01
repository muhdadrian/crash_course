# Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# reverse() doesn't sort backwardly alphabetically, it simply reverses the order of the list

# reverse() method changes the order of a list permanently, but you can revert to the original order
# anytime by applying reverse() to the same list a second time

cars.reverse()
print(cars)