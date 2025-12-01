# Looping Through a Slice
# we loop through the first three players and print their names as part of a simple roster:

players = ['adrian', 'hafizah', 'sarah', 'fatih', 'fariq']

print("Here are the first three players on my team:")
for player in players[:3]:# Python loops through only the first three names
    print(player.title())