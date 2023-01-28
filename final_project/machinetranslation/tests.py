import unittest
from translator import english_to_french,french_to_english
class TestStringMethods(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_error(self):
        self.assertRaises(Exception,english_to_french(None))
        self.assertRaises(Exception,french_to_english(None))

if __name__ == '__main__':
    unittest.main()