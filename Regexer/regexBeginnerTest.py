import unittest
from regexBeginner import *

"""
    This unit test is not perfect. It also shows the print statements from the called functions.
"""


class Tester(unittest.TestCase):
    def test_file_extension(self):
        self.assertEqual(file_extension("helloWorld.py"), ".py")
        self.assertEqual(file_extension("package.json"), ".json")
        self.assertNotEqual(file_extension("index.html"), ".Html")
        self.assertNotEqual(file_extension("effects.css"), ".CSS")

    def test_a3bs(self):
        self.assertTrue(aFollowedByThreeBs("aaabbbb"))
        self.assertTrue(aFollowedByThreeBs("ababababbbb"))
        self.assertFalse(aFollowedByThreeBs("ababababb"))
        self.assertFalse(aFollowedByThreeBs("abbabb"))

    def test_valid_fraction(self):
        self.assertTrue("1/32")
        self.assertTrue("98/54")
        self.assertTrue("9/22")
        self.assertTrue("12/1")


if __name__ == "__main__":
    unittest.main()
