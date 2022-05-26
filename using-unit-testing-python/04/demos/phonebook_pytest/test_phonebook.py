import unittest

from phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook()

    # def tearDown(self) -> None:
    #     pass


    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEquals("12345",number)
        




    def test_missing_name(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("Missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        
        
        


    def test_is_consistent_with_diff_entries(self):
        self.phonebook.add("Dave",55555)
        self.phonebook.add("Mary",12345)
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_is_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Dave",55555) 
        self.phonebook.add("Mary",55555)
        self.assertFalse(self.phonebook.is_consistent()) 
    
    def test_is_consistent_with_dupe_prefix(self):
        self.phonebook.add("",12345)
        self.phonebook.add("",12345)
    
    
    # def test_is_consistent_with_diff_entries(self):
    




if __name__ == '__main__':
        unittest.main()
        
        



# def test_lookup_by_name(phonebook):
#     phonebook.add("Bob", "1234")
#     assert "1234" == phonebook.lookup("Bob")


# def test_phonebook_contains_all_names(phonebook):
#     phonebook.add("Bob", "1234")
#     assert "Bob" in phonebook.names()



