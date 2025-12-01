# Now we can write a simple loop to count the words in any text we want to analyze. We do this by storing the names of the files we want to analyze in a list, and then we call count_words() for each file in the list. 

# We’ll try to count the words for Syukuri, Tiada, Learn, and Tujuan Hidup, which are all available in the public domain. I’ve intentionally left tiada.txt out of the directory containing word_count.py, so we can see how well our program handles a missing file:

def count_words(filename):
    """Count the approximate number of words in a file.""" #1
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['syukuri.txt', 'tiada.txt', 'learn.txt', 'tujuan_hidup.txt']
for filename in filenames:
    count_words(filename)

# The missing tiada.txt file has no effect on the rest of the program’s execution:

# Using the try-except block in this example provides two significant advantages. We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find. 

# If we don’t catch the FileNotFoundError that tiada.txt raised, the user would see a full traceback, and the program would stop running after trying to analyze Tiada. It would never analyze Learn or Tujuan Hidup.
