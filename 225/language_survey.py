# To show that the AnonymousSurvey class works, let’s write a program that uses the class:

from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


# This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with that question. 

# The program calls show_question() to display the question and then prompts for responses. Each response is stored as it is received. When all responses have been entered (the user inputs q to quit), show_results() prints the survey results:

# What language did you first learn to speak?
# Enter 'q' at any time to quit.

# Language: English 
# Language: Spanish 
# Language: English 
# Language: Mandarin 
# Language: q

# Thank you to everyone who participated in the survey!
# Survey results:
# - English
# - Spanish
# - English
# - Mandarin

# This class works for a simple anonymous survey. But let’s say we want to improve AnonymousSurvey and the module it’s in, survey. We could allow each user to enter more than one response. 

# We could write a method to list only unique responses and to report how many times each response was given. 

# We could write another class to manage nonanonymous surveys.

# Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. 

# For example, it’s possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. 

# To ensure we don’t break existing behavior as we develop this module, we can write tests for the class.



# ChatGPT

# my_survey = AnonymousSurvey(question)

# AnonymousSurvey(question): This is a call to the constructor method __init__ of the AnonymousSurvey class. 

# This constructor method is defined with def __init__(self, question):. 

# It initializes a new instance of the AnonymousSurvey class. The question parameter is passed to this constructor method, allowing you to specify the survey question when creating a new survey object.

# my_survey: This is a variable name chosen to refer to the instance of the AnonymousSurvey class that is created by calling the constructor. 

# By assigning the result of the constructor call to my_survey, you're creating a new instance of the AnonymousSurvey class and storing it in this variable. 

# This variable can then be used to interact with the methods and properties of the AnonymousSurvey object.

# my_survey.show_question()

# my_survey: This refers to the instance of the AnonymousSurvey class that was created earlier. 

# Since my_survey now holds an instance of AnonymousSurvey, you can call its methods.

# show_question(): This is a method defined within the AnonymousSurvey class. When called on an instance of AnonymousSurvey, it prints the survey question to the console. 

# This method simply displays the survey question stored in the instance.

# So, these two lines of code together create a new AnonymousSurvey object with a specified question and then display that question to the user.
