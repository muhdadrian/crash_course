import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin'] #1
        for response in responses:
            my_survey.store_response(response)

        for response in responses: #2
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()


# We call the new method test_store_three_responses(). We create a survey object just like we did in test_store_single_response(). We define a list containing three different responses #1, and then we call store_response() for each of these responses. 

# Once the responses have been stored, we write another loop and assert that each response is now in my_survey.responses #2.

# When we run test_survey.py again, both tests (for a single response and for three responses) pass:

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK

# This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of unittest to make them more efficient.


