import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        with self.assertRaises(Exception):  
            english_to_french()  # Null input

class test_french_to_english(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        with self.assertRaises(Exception):
            french_to_english()  # Null input

unittest.main()