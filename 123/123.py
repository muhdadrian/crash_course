# The program at 122.py works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

