import unittest

#A testcase is created by subclassing unittest.TestCase.
class SnowRescueServiceTest(unittest.TestCase):

    #tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.
    def test_start_here(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()

