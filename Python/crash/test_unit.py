import unitest
import name_function 

class NamesTestCase(unitest.TestCase):
    """Tests for 'name_function.py'. """
    def test_first_last_name(self):
        """Do names like 'janis joplin' work?"""
        name = formatted_name('janis', 'joplin')
        self.asserEqual(name, 'Janis Joplin')

        unitest.main()
