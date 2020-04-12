import unittest
from algorithms.hacker_rank.MinimumSwaps2 import MinimumSwaps2

class TestsMinimumSwaps2(unittest.TestCase):

    def test_get_minimum_swaps_to_sort_array_1(self):
        arr = [7, 1, 3, 2, 4, 5, 6]

        tests_minimum_swaps_2 = MinimumSwaps2()

        self.assertEqual(5, tests_minimum_swaps_2.get_minimum_swaps_to_sort_array(arr))
