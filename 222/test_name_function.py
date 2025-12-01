import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()


# This time, running the file test_name_function.py gives this output:

# E #1

# ======================================================================

# ERROR: test_first_last_name (__main__.NamesTestCase) #2

# ----------------------------------------------------------------------
# Traceback (most recent call last): #3
# File "test_name_function.py", line 8, in test_first_last_name
#        formatted_name = get_formatted_name('janis', 'joplin')
#    TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# ----------------------------------------------------------------------

# Ran 1 test in 0.000s #4

# FAILED (errors=1) #5

# There’s a lot of information here because there’s a lot you might need to know when a test fails. 

# The first item in the output is a single E #1, which tells us one unit test in the test case resulted in an error. 

# Next, we see that test_first_last_name() in NamesTestCase caused an error #2. 

# Knowing which test failed is critical when your test case contains many unit tests. 

# At #3 we see a standard traceback, which reports that the function call get_formatted_name('janis', 'joplin') no longer works because it’s missing a required positional argument.

# We also see that one unit test was run #4. Finally, we see an additional message that the overall test case failed and that one error occurred when running the test case #5. 

# This information appears at the end of the output so you see it right away; you don’t need to scroll up through a long output listing to find out how many tests failed.

