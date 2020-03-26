import unittest
from hacker_rank.PairOfSocks import PairOfSocks


class TestsPairOfSocks(unittest.TestCase):

    def test_find_pairs(self):
        A = [9, 3, 9, 3, 9, 7, 9]

        pair_of_socs = PairOfSocks()

        self.assertEqual(3, pair_of_socs.find_no_of_pairs(A))


if __name__ == '__main__':
    unittest.main()
