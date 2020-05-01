import unittest
from algorithms.hacker_rank.LeftRotationArray import LeftRotation


class TestsLeftRotation(unittest.TestCase):

    def test_left_rotation_by_value(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        d = 4
        left_rotation = LeftRotation()
        self.assertEqual("5 1 2 3 4", left_rotation.left_rotation_by_value(A, n, d))

    def test_left_rotation_by_index(self):
        A = [1, 2, 3, 4, 5]
        d = 4
        left_rotation = LeftRotation()
        self.assertEqual("5 1 2 3 4", left_rotation.left_rotation_by_index(A, d))


if __name__ == '__main__':
    unittest.main()
