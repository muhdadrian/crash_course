# at #info below, you could expand the loop by adding an elif block that turns yellow aliens into red, fast-moving ones worth 15_numbers points each.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': #info
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5_strings aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# It's common to store a number of dictionaries in a list when each dictionary contains many kinds of information about one object. 

# For example, you might create a dictionary for each user on a website,and store the individual dictionaries in a list called users.

# All of the dictionaries in the list should have an identical structure so you can loop through the list and work with each dictionary object in the same way.
