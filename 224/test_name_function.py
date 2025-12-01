import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name( #1
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
        unittest.main()


# We name this new method test_first_last_middle_name(). The method name must start with test_ so the method runs automatically when we run test_name_function.py. 

# We name the method to make it clear which behavior of get_formatted_name() we’re testing. As a result, if the test fails, we know right away what kinds of names are affected. 

# It’s fine to have long method names in your TestCase classes. They need to be descriptive so you can make sense of the output when your tests fail, and because Python calls them automatically, you’ll never have to write code that calls these methods.

# To test the function, we call get_formatted_name() with a first, last, and middle name #1, and then we use assertEqual() to check that the returned full name matches the full name (first, middle, and last) that we expect. When we run test_name_function.py again, both tests pass:

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK

# Great! We now know that the function still works for names like Janis Joplin, and we can be confident that it will work for names like Wolfgang Amadeus Mozart as well.



