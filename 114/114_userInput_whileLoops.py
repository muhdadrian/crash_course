# How the input() Function Works

# The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.

# For example, the following program asks the user to enter some text, then displays that message back to the user:

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# The input() function takes one argument: the prompt, or instructions, that we want to display to the user so they know what to do. 
 
# In this example, when Python runs the first line, the user sees the prompt 'Tell me something, and I will repeat it back to you:'.

# The program waits while the user enters their response and continues after the user presses ENTER.

# The response is assigned to the variable message, then print(message) displays the input back to the user.
