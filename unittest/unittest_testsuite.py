import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestDictionarys(unittest.TestCase):
    dictionary = {"Correct":1, " Wrong":2, " No match":4, "This matchs":3}
    keylist = ["Correct", "This matchs", "Non existing"]

    # check if the keys have the right format
    def test_key_format(self):
        for key in self.dictionary.keys():

            with self.subTest(key = key):

                self.assertRegex(key, '^[^\s]+[a-zA-Z0-9]+')

    # check if the need keys for the specific modules are appended
    def test_key_existing(self):
        dict_keys =  self.dictionary.keys()

        for key in self.keylist:
            with self.subTest(key = key):
                self.assertIn(key, dict_keys)


if __name__ == '__main__':
    unittest.main()