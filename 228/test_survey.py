# THIS IS NOT WORKING AS ALL TEST PASSED. REFER TO 3RD EDITION.

# The setUp() Method

# In test_survey.py we created a new instance of AnonymousSurvey in each test method, and we created new responses in each method. 

# The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods. 

# When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_. 

# Any objects created in the setUp() method are then available in each test method you write.

# Let’s use setUp() to create a survey instance and a set of responses that can be used in test_store_single_response() and test_store_three_responses():

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) #1
        self.responses = ['English', 'Spanish', 'Mandarin'] #2

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()


# The method setUp() does two things: it creates a survey instance #1, and it creates a list of responses #2. 

# Each of these is prefixed by self, so they can be used anywhere in the class. 

# This makes the two test methods simpler, because neither one has to make a survey instance or a response. 

# The method test_store_single_response() verifies that the first response in self.responses—self.responses[0]—can be stored correctly, and test_store _three_responses() verifies that all three responses in self.responses can be stored correctly.

# When we run test_survey.py again, both tests still pass. These tests would be particularly useful when trying to expand AnonymousSurvey to handle multiple responses for each person. 

# After modifying the code to accept multiple responses, you could run these tests and make sure you haven’t affected the ability to store a single response or a series of individual responses.

# When you’re testing your own classes, the setUp() method can make your test methods easier to write. 

# You make one set of instances and attributes in setUp() and then use these instances in all your test methods. 

# This is much easier than making a new set of instances and attributes in each test method.

# When a test case is running, Python prints one character for each unit test as it is completed. 

# A passing test prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an F. 

# This is why you’ll see a different number of dots and characters on the first line of output when you run your test cases. 

# If a test case takes a long time to run because it contains many unit tests, you can watch these results to get a sense of how many tests are passing.
