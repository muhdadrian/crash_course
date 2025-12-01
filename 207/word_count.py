# Working with Multiple Files

# Let’s add more books to analyze. But before we do, let’s move the bulk of this program to a function called count_words(). By doing so, it will be easier to run the analysis for multiple books:

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


filename = 'syukuri.txt'
count_words(filename)

# It’s a good habit to keep comments up to date when you’re modifying a program, so we changed the comment to a doc-string and reworded it slightly at #1.