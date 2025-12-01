# Sometimes you'll want to write a prompt that's longer than one line. For example, you might want to tell the user why you're asking for certain input. 

# You can assign your prompt to a variable and pass that variable to the input() function. This allows you to build your prompt over several lines, then write a clean input() statement.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# The example above shows one way to build a multi-line string. The first line assigns the first part of the message to the variable prompt. 

# In the second line, the operator += takes the string that was assigned to prompt and adds the new string onto the end.

# The prompt now spans two lines, again with space after the question mark for clarity. 
