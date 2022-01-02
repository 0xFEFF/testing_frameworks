# This document should show how to use nose2

# finds every test that starts with test
# modules that name starts with test

# loads tests form unittest.TestCase subclassens and all functions that start with test

# Naming Tests
"""

"""

#nose loads test modules lazily: tests in the first-loaded module are executed before the second module is imported. nose2 loads all tests first, then begins test execution. This has some important implications.