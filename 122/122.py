# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:" #1
prompt += "\nEnter 'quit' to end the program. "
message = "" #2
while message != 'quit': #3
    message = input(prompt)
    print(message)

# At 1, we define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit').

# Then we set up a variable message at 2 to keep track of whatever value the user enters. We define message as an empty string, "", so Python has something to check the first time it reaches the while line. 

# The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet. 

# If Python has nothing to compare, it won’t be able to continue running the program. To solve this problem, we make sure to give message an initial value. 

# Although it’s just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work.

# This while loop at 3 runs as long as the value of message is not 'quit'.

# The first time through the loop, message is just an empty string, so Python enters the loop. 

# At message = input(prompt), Python displays the prompt and waits for the user to enter their input. 

# Whatever they enter is assigned to message and printed; then, Python reevaluates the condition in the while statement. 

# As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. 

# When the user finally enters 'quit', Python stops executing the while loop and the program ends.

