import unittest
from algorithms.hacker_rank.JumpingOnClouds import JumpingOnClouds


class TestsJumpingOnClouds(unittest.TestCase):

    def test_jumps(self):
        A = [0, 1, 0, 0, 0, 1, 0]
        jumping_on_clouds = JumpingOnClouds()
        self.assertEqual(3, jumping_on_clouds.count_jumps(A))


if __name__ == '__main__':
    unittest.main()
