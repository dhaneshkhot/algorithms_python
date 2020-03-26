import unittest
from codility_tests.BinaryGap import BinaryGap


class TestsBinaryGap(unittest.TestCase):
    def test_binary_gap(self):
        number = 187838748

        binary_gap = BinaryGap()

        self.assertEqual(3, binary_gap.solution(number))
