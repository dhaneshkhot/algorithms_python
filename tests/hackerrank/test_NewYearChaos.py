import unittest
from algorithms.hacker_rank.NewYearChaos import NewYearChaos


class TestsNewYearChaos(unittest.TestCase):

    def test_get_minimum_bribes_1(self):
        arr = [2, 1, 5, 3, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual(3, new_year_chaos.get_minimum_bribes_with_bubble_sort(arr))

    def test_get_minimum_bribes_2(self):
        arr = [2, 5, 1, 3, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual("Too chaotic", new_year_chaos.get_minimum_bribes_with_bubble_sort(arr))

    def test_get_minimum_bribes_3(self):
        arr = [2, 1, 5, 3, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual(3, new_year_chaos.get_minimum_bribes_with_index(arr))

    def test_get_minimum_bribes_4(self):
        arr = [2, 5, 1, 3, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual("Too chaotic", new_year_chaos.get_minimum_bribes_with_index(arr))

    def test_get_minimum_bribes_5(self):
        arr = [1, 2, 5, 3, 7, 8, 6, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual(7, new_year_chaos.get_minimum_bribes_with_bubble_sort(arr))

    def test_get_minimum_bribes_6(self):
        arr = [1, 2, 5, 3, 7, 8, 6, 4]
        new_year_chaos = NewYearChaos()
        self.assertEqual(7, new_year_chaos.get_minimum_bribes_with_index(arr))


if __name__ == '__main__':
    unittest.main()
