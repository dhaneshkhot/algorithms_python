import unittest
from algorithms.hacker_rank.Palidrome import Palindrome

class TestPalidnrome(unittest.TestCase):

    def test_if_palindrome_1(self):
        p = Palindrome()
        self.assertEqual(True, p.check_if_palidrome("abccba"))

    def test_if_palindrome_2(self):
        p = Palindrome()
        self.assertEqual(True, p.check_if_palidrome("abcba"))

    def test_if_palindrome_3(self):
        p = Palindrome()
        self.assertEqual(False, p.check_if_palidrome("acba"))

    def test_if_palindrome_4(self):
        p = Palindrome()
        self.assertEqual(True, p.check_if_palidrome("tacocat"))

    def test_get_palindrome_substring_1(self):
        p = Palindrome()
        self.assertEqual("coc", p.get_palindrome_substring("tacocatac"))

    def test_get_palindrome_substring_2(self):
        p = Palindrome()
        self.assertEqual("ata", p.get_palindrome_substring("tacobcataac"))

    def test_get_palindrome_substring_3(self):
        p = Palindrome()
        self.assertEqual("tt", p.get_palindrome_substring("oabcattacocatmapc"))


if __name__ == '__main__':
    unittest.main()