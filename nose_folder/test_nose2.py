# in test_simple.py
import unittest2

import nose2
from nose2.tools import params

import re


class TestStrings(unittest2.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")


@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')

class DicitonaryTests():
    def setUp(self):
        self.dictionary = {"Correct":1, " Wrong":2, " No match":4, "This matchs":3}

    def test_dictionary(self):
        
        for key in self.dictionary.keys():
            assert re.match('^[^\s]+[a-zA-Z0-9]+', key)


