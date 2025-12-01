# Nesting
# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] #1

for alien in aliens:
    print(alien)

# We first create three dictionaries, each representing a different alien. 

# At 1, we store each of these dictionaries in a list called aliens. 

# Finally, we loop through the list and print out each alien.
