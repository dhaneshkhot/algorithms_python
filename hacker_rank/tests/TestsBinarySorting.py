import unittest
from hacker_rank.BinarySorting import BinarySorting


class TestsBinarySorting(unittest.TestCase):

    def test_binary_sorting(self):
        A = [7, 8, 5, 6]

        test_binary_sorting = BinarySorting()

        self.assertEqual(['1000', '0101', '0110', '0111'], test_binary_sorting.rearrange(A))


if __name__ == '__main__':
    unittest.main()
