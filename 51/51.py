# Copying a List

# To copy a list, you can make a slice that includes the entire original list by omitting the first
# index and the second index([:]). This tells Python to make a slice that starts at the first item and
# ends with the last item, producing a copy of the entire list.
#
# For example, imagine we have a list of our favorite foods and want to make a separate list of foods
# that a friend likes. This friend likes everything in our list so far, so we can create their list
# by copying ours:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)