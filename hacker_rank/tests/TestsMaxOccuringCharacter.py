import unittest
from hacker_rank.MaxOccuringCharacter import MaxOccuringCharacter


class TestsMaxOccuringCharacter(unittest.TestCase):

    def test_max_occuring_character(self):
        text = "abbbaacc"

        test_max_occuring_character = MaxOccuringCharacter()

        self.assertEqual('a', test_max_occuring_character.maximum_occurring_character(text))


if __name__ == '__main__':
    unittest.main()
