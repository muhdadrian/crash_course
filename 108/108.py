# All the aliens have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually.


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Because we want to modify the first three aliens, we loop through a slice that includes only the first three aliens. 

# All of the aliens are green now but that won't always be the case, so we write an if statement to make sure we're only modifying green aliens. 

# If the alien is green, we change the color to 'yellow', the speed to 'medium', and the point value to 10, as shown in the output.

