# to prove that we have two separate lists, we'll add a new food to each list and show that each list
# keeps track of the appropriate person's favorite foods:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)