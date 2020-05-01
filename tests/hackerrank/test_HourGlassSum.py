import unittest
from algorithms.hacker_rank.HourGlassSum import HourGlassSum


class TestHourGlassSum(unittest.TestCase):

    def test_get_hour_glass_sum(self):
        arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
               [0, 0, 1, 2, 4, 0]]
        hour_glass_sum = HourGlassSum()
        self.assertEqual(19, hour_glass_sum.hourglassSum(arr))


if __name__ == '__main__':
    unittest.main()
