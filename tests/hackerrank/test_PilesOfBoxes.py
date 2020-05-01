import unittest
from algorithms.hacker_rank.PilesOfBoxes import PilesOfBoxes


class TestPilesOfBoxes(unittest.TestCase):

    def test1(self):
        boxes_in_piles = [4, 5, 5, 2, 4]
        p = PilesOfBoxes()
        self.assertEqual(6, p.get_no_of_steps_to_move_boxes(boxes_in_piles))

    def test2(self):
        boxes_in_piles = [4, 886, 777, 915, 1793]
        p = PilesOfBoxes()
        self.assertEqual(10, p.get_no_of_steps_to_move_boxes(boxes_in_piles))

    def test3(self):
        boxes_in_piles = [5, 6, 7, 15, 6, 8, 9, 10, 6, 7]
        p = PilesOfBoxes()
        self.assertEqual(25, p.get_no_of_steps_to_move_boxes(boxes_in_piles))


if __name__ == '__main__':
    unittest.main()
