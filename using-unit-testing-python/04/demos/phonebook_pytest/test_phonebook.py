import unittest

from phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):


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
        phonebook = Phonebook()
        self.assertTrue(phonebook.is_consistent())
        



# def test_lookup_by_name(phonebook):
#     phonebook.add("Bob", "1234")
#     assert "1234" == phonebook.lookup("Bob")


# def test_phonebook_contains_all_names(phonebook):
#     phonebook.add("Bob", "1234")
#     assert "Bob" in phonebook.names()



