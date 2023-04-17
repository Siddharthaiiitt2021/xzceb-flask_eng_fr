from translator import english_to_french, french_to_english
import unittest

class e2fTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(''),'')

class f2eTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''),'')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
