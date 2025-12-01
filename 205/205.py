# Analyzing Text

# Let’s pull in the text of Alice in Wonderland and try to count the number of words in the text.

# We’ll use the string method split(), which can build a list of words from a string. Here’s what split() does with a string containing just the title "Alice in Wonderland":

title = "Alice in Wonderland"
print(title.split())


>>> title = "Alice in Wonderland" 
>>> title.split()
['Alice', 'in', 'Wonderland']

# The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list. 

# The result is a list of words from the string, although some punctuation may also appear with some of the words.
