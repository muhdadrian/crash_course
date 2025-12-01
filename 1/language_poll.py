import unittest
from poll import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """to test the AnonyousSurvey Class in poll.py"""

    def setUp(self):
        """make a survey and store responses"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'malay', 'dusun']

    def test_single_response(self):
        """test a single response"""
        self.responses
        

    
    
    # def test_three_response(self):
    #     """test a single response"""
    #     question = "What language did you first learn to speak?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['english', 'malay', 'dusun']

    #     for response in responses:
    #         my_survey.store_response(response)

    #     for response in responses:
    #         self.assertIn(response, my_survey.responses)
        
        

if __name__ == "__main__":
    unittest.main()

