import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'. """
    def test_first_last_name(self): #“Any method that starts with test_ will be run automatically when we run program ”
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin','K')
        self.assertEqual(formatted_name, 'Janis K Joplin') #“Assert methods verify that a result you received matches the result you expected to receive.”
#“Compare the value in formatted_name to the string 'Janis Joplin'. If they are equal as expected, fine. But if they don’t match, let me know!”
unittest.main()
