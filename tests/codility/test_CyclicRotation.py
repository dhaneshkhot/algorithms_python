import unittest
from algorithms.codility_tests.CyclicRotation import CyclicRotation


class CyclicRotationTests(unittest.TestCase):

    def test_cyclic_rotation(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        cyclic_rotation = CyclicRotation()
        self.assertEqual([9, 7, 6, 3, 8], cyclic_rotation.cyclic_rotate_array(A, K))


if __name__ == '__main__':
    unittest.main()
