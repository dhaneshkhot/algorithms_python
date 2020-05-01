import unittest
from algorithms.hacker_rank.BubbleSort import BubbleSort


class TestsBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [6, 4, 1]
        bubble_sort = BubbleSort()
        self.assertEqual([3, 1, 6], bubble_sort.get_num_of_swaps_with_bubble_sort(arr))


if __name__ == '__main__':
    unittest.main()
