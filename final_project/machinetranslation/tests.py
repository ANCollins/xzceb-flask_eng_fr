"""Test cases for French to English translations."""
import unittest
from translator import english_to_french,french_to_english

# Test cases for English to French translations.
class TestEnglishToFrench(unittest.TestCase):
    # Andre Collins
    def test_english_to_french(self):        
        # Checks for an empty returns.
        self.assertNotEqual(english_to_french(0), 0)
        # Test for the translation of the word ‘Hello’ and ‘Bonjour’.
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        # Test for the translation of the word ‘Good Day’ and ‘Bonne journée’.
        self.assertEqual(english_to_french('Good Day'),'Bonne journée')
        # Test for the translation of the word ‘Good Afternoon’ and ‘Bon après-midi’.
        self.assertEqual(english_to_french('Good Afternoon'),'Bon après-midi')

# Test cases for French to English translations.
class TestFrenchToEnglish(unittest.TestCase):
    # Andre Collins
    def test_french_to_english(self):
        # Checks for an empty field or null.
        self.assertNotEqual(french_to_english(0), 0)
        # Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        # Test for the translation of the word ‘Bonne journée’ and ‘Good Day’.
        self.assertEqual(french_to_english('Bonne journée'),'Good Day')
        # Test for the translation of the word ‘Bon après-midi’ and ‘Good Afternoon’.
        self.assertEqual(french_to_english('Bon après-midi'),'Good Afternoon')

if __name__ == '__main__':
    unittest.main()