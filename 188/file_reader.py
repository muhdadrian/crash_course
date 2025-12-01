filename = 'pi_digits.txt' #1

with open(filename) as file_object: #2
    for line in file_object: #3
        print(line)


# At #1 we assign the name of the file we’re reading from to the variable filename. This is a common convention when working with files. 

# Because the variable filename doesn’t represent the actual file — it’s just a string telling Python where to find the file—you can easily swap out 'pi_million_digits.txt' for the name of another file you want to work with. 

# After we call open(), an object representing the file and its contents is assigned to the variable file_object #2 

# We again use the with syntax to let Python open and close the file properly. To examine the file’s contents, we work through each line in the file by looping over the file object #3

# When we print each line, we find even more blank lines:
