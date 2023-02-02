from translator import englishToFrench,frenchToEnglish
import unittest

"""
Test cases for English to French translations.
"""
class testEnglishToFrench(unittest.TestCase):
    # Andre Collins
    def test_englishToFrench(self):
        
        # Checks for an empty field or null.
        self.assertEqual(englishToFrench(''),'Empty')
        # Test for the translation of the word ‘Hello’ and ‘Bonjour’.
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        # Test for the translation of the word ‘Good Day’ and ‘Bonne journée’.
        self.assertEqual(englishToFrench('Good Day'),'Bonne journée')
        # Test for the translation of the word ‘Good Afternoon’ and ‘Bon après-midi’.
        self.assertEqual(englishToFrench('Good Afternoon'),'Bon après-midi')
        # Test to see if the inputs are not equal
        self.assertNotEqual(englishToFrench('Good Afternoon'),'Bon après-midi')
        # Test to see if the inputs are not equal
        self.assertNotEqual(englishToFrench('Good Afternoon'),'Good Afternoon')

"""
Test cases for French to English translations.
"""
class testFrenchToEnglish(unittest.TestCase):
    # Andre Collins
    def test_frenchToEnglish(self):

        # Checks for an empty field or null.
        self.assertEqual(frenchToEnglish(''),'Empty')
        # Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')        
        # Test for the translation of the word ‘Bonne journée’ and ‘Good Day’.
        self.assertEqual(frenchToEnglish('Bonne journée'),'Good Day')
        # Test for the translation of the word ‘Bon après-midi’ and ‘Good Afternoon’.
        self.assertEqual(frenchToEnglish('Bon après-midi'),'Good Afternoon')
        # Test to see if the inputs are not equal
        self.assertNotEqual(frenchToEnglish('Bon après-midi'),'Good Afternoon')
        # Test to see if the inputs are not equal
        self.assertNotEqual(frenchToEnglish('Bon après-midi'),'Bon après-midi')

unittest.main()