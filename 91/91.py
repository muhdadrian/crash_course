alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow': #1
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment #2

print(f"New x_position: {alien_0['x_position']}")

# At 1, an if-elif-else chain determines how far the alien should move to the right and assigns this
# value to the variable x_increment. If the alien's speed is 'slow', it moves one unit to the right;
# if the speed is 'medium', it moves two units to the right; and if it's 'fast', it moves three units
# to the right. Once the increment has been calculated, it's added to the value of x_position at 2,
# and the result is stored in the dictionary's x-position.
#
# Because this is a medium-speed alien, its position shifts two units to the right:
