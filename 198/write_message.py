# Appending to a File

# If you want to add content to a file instead of writing over existing content, you can open the file in append mode. 

# When you open a file in append mode, Python doesn’t erase the contents of the file before returning the file object. 

# Any lines you write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.

# Let’s modify write_message.py by adding some new reasons we love programming to the existing file programming.txt:

filename = 'programming.txt'
with open(filename, 'a') as file_object: #1
    file_object.write("I also love finding meaning in large datasets.\n") #2
    file_object.write("I love creating apps that can run in a browser.\n")


# At #1 we use the 'a' argument to open the file for appending rather than writing over the existing file. 

# At #2 we write two new lines, which are added to programming.txt:

# I love programming.
# I love creating new games.
# I also love finding meaning in large datasets.
# I love creating apps that can run in a browser.

# We end up with the original contents of the file, followed by the new content we just added.
