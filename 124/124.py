# Using a Flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True #1
while active: #2
    message = input(prompt)

    if message == 'quit': #3
        active = False
    else: #4
        print(message)

# We set the variable active to True at 1 so the program starts in an active state. 
 
# Doing so makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program. 

# As long as the active variable remains True, the loop will continue running at 2.

# In the if statement inside the while loop, we check the value of message once the user enters their input. 

# If the user enters 'quit' at 3, we set active to False, and the while loop stops. 

# If the user enters anything other than 'quit' at 4, we print their input as a message.

# This program has the same output as the previous example where we placed the conditional test directly in the while statement. 

# But now that we have a flag to indicate whether the overall program is in an active state, it would be easy to add more tests (such as elif statements) for events that should cause active to become False. 

# This is useful in complicated programs like games in which there may be many events that should each make the program stop running. 

# When any of these events causes the active flag to become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.
