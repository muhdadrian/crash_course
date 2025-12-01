# You can also use the remove() method to work with a value that's being removed from a list.
# Let's remove the value 'ducati' and print a reason for removing it from the list


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']# we define the list
print(motorcycles)

too_expensive = 'ducati' # we assign the value 'ducati' to a variable called too_expensive
motorcycles.remove(too_expensive)# we use the var too_expensive to tell Python which value to remove from the list
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# The value 'ducati' has been removed from the list but is still accessible through the var too_
# expensive, allowing us to print statement about why we removed 'ducati' from the list of
# motorcycles
