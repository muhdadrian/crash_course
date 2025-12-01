# Removing an Item by Value
# Sometimes you won't know the position of the value you want to remove from a list.
# If you only know the value of the item you want to remove, you can use the remove() method.


# we remove the value 'ducati'
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') # this will tell Python to figure out where 'ducati' appears in the list and remove that element
print(motorcycles)
