import unittest
from algorithms.hacker_rank.CountingValleys import CountingValleys


class TestsCountingValleys(unittest.TestCase):

    def test_count_valleys(self):
        A = "UDDDUDUU"
        counting_valleys = CountingValleys()
        self.assertEqual(1, counting_valleys.count_valleys(A))

    def test_count_valleys2(self):
        A = "DDUUUUDDDU"
        counting_valleys = CountingValleys()
        self.assertEqual(2, counting_valleys.count_valleys(A))


if __name__ == '__main__':
    unittest.main()
