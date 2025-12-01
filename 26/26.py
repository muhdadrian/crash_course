# Popping Items from any Position in a list
# You can use pop() to remove an item from any position in a list by including the index of the
# item you want to remove in parentheses


motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# each time you use pop(), the item you work with is no longer stored in the list.
# if you're unsure whether to use the del statement or the pop() method:
# 1) to delete an item from a list and not using that item in any way, use the del statement
# 2) if you want to use an item as you remove it, use the pop() method
