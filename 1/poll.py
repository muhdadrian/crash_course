class AnonymousSurvey:
    """collect survey about language you learn"""

    def __init__(self, question):
        """prepare question and ready to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show question"""
        print(self.question)

    def store_response(self, new_response):
        """store responses"""
        self.responses.append(new_response)

    def show_result(self):
        """print survey result"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


    
        