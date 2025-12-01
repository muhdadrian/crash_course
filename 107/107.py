# A more realistic example would involve more than three aliens with code that automatically generates each alien. 

# In the following example we use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30): #1
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #2
    aliens.append(new_alien) #3

# Show the first 5 aliens.
for alien in aliens[:5]: #4
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}") #5

# The example above begins with an empty list to hold all of the aliens that will be created. 

# At #1, range() returns a series of numbers, which just tells Python how many times we want the loop to repeat. 

# Each time the loop runs we create a new alien at #2, and then append each new alien to the list aliens at #3. 

# At #4, we use slice to print the first five aliens, and then at #5, we print the

# length of the list to prove we've actually generated the full fleet of 30 aliens.