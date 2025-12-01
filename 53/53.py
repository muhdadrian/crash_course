# if we had simply set 'friend_foods = my_foods', we would not produce two separate lists. For example,
# here's what happens when you try to copy a list without using slicing:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods # This doesn't work. Both variables point to the same list.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)