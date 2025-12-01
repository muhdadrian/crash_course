# Testing the AnonymousSurvey Class

# Let’s write a test that verifies one aspect of the way AnonymousSurvey behaves. 

# We’ll write a test to verify that a single response to the survey question is stored properly. We’ll use the assertIn() method to verify that the response is in the list of responses after it’s been stored:

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): #1
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self): #2
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) #3
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) #4

if __name__ == '__main__':
    unittest.main()


# We start by importing the unittest module and the class we want to test, AnonymousSurvey. 

# We call our test case TestAnonymousSurvey, which again inherits from unittest.TestCase #1. 

# The first test method will verify that when we store a response to the survey question, the response ends up in the survey’s list of responses. 

# A good descriptive name for this method is test_store_single_response() #2. 

# If this test fails, we’ll know from the method name shown in the output of the failing test that there was a problem storing a single response to the survey.

# To test the behavior of a class, we need to make an instance of the class. At #3 we create an instance called my_survey with the question "What language did you first learn to speak?" We store a single response, English, using the store_response() method. Then we verify that the response was stored correctly by asserting that English is in the list my_survey.responses #4.

# When we run test_survey.py, the test passes:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# OK

# This is good, but a survey is useful only if it generates more than one response. 

# Let’s verify that three responses can be stored correctly. To do this, we add another method to TestAnonymousSurvey in 227:
