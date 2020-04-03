import unittest
from algorithms.hacker_rank.DiagonalDifference import DiagonalDifference


class TestsDiagonalDifference(unittest.TestCase):

    def test_diagonal_difference(self):
        matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

        diagonal_difference = DiagonalDifference()

        self.assertEqual(2, diagonal_difference.get_diagonal_difference(matrix))