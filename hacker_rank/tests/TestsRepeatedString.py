import unittest
from hacker_rank.RepeatedString import RepeatedString


class TestsRepeatedString(unittest.TestCase):

    def test_count(self):
        A = "abcac"
        no_of_chars_to_consider = 10

        repeated_string = RepeatedString()

        self.assertEqual(4, repeated_string.count_occurances_of_a_character(A, no_of_chars_to_consider))

    def test_count2(self):
        A = "a"
        no_of_chars_to_consider = 1000000000000

        repeated_string = RepeatedString()

        self.assertEqual(1000000000000, repeated_string.count_occurances_of_a_character(A, no_of_chars_to_consider))