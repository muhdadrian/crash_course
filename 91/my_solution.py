alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'sl'}
print(f"Original x_position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    alien_0['x_position'] += 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] += 2
else:
    alien_0['x_position'] += 3

print(f"New x_position: {alien_0['x_position']}")