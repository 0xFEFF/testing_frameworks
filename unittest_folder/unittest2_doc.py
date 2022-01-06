# This document should show how to use unittest2 

# test fixture
"""
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

@
"""

# test case
"""
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

subclass from unittest2.TestCase 

methods start with test

need to use assert*() provided by TestCase

setUp(self) wird vor jeder Ausführung ausgeführt
tearDown(self)

@unittest.skip("demonstrating skipping")
@unittest.skipIf(mylib.__version__ < (1,3), "not supported")
@unittest2.skipUnless(sys.platform.startswith("win"), "requires windows")
@unittest.expectedFailure

@unittest.skip() can also be used for classes


subTest() used for multiple Tests

"""

# test suite
"""
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
"""

# test runner
"""
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
"""

# Basic Example

import unittest2

"""class TestStringMethods(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()"""


# tests need to start with the name test to inform the runner which test should be exectued
"""
tests needs to call
    assertEqual() to check for a expected result
    assertTrue() to check a condition
    assertFalse() to check a condition
    assertRaises() to verify that a specific exception gets raised

this is used instead of assert
"""

# test cases are represented as instances of unittest.TestCase
# the order of test is determined by sorting the test method names with respect to the built in ordering for strings

""""import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')"""

# decorator to show that task should be skiped or are intended to fail but dont are errors

"""class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass"""

# distinguishing test iterations using subtests
# subTest() context manager is used

class NumbersTest(unittest2.TestCase):

    def test_even(self):
        # Test that numbers between 0 and 5 are all even.
        
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
