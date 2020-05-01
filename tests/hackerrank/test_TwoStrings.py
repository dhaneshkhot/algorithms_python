import unittest
from algorithms.hacker_rank.TwoStrings import TwoStrings


class TestsTwoStrings(unittest.TestCase):

    def test_do_they_share_common_substring_1(self):
        s1 = "hello"
        s2 = "world"

        two_strings = TwoStrings()
        self.assertEqual("YES", two_strings.do_they_share_common_substring(s1, s2))

    def test_do_they_share_common_substring_2(self):
        s1 = "hi"
        s2 = "world"

        two_strings = TwoStrings()
        self.assertEqual("NO", two_strings.do_they_share_common_substring(s1, s2))


if __name__ == '__main__':
    unittest.main()
