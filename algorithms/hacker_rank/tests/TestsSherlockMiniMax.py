import unittest
from algorithms.hacker_rank import SherlockMiniMax


class TestsSherlockMiniMax(unittest.TestCase):

    def test_sherlock_minimax_1(self):
        arr = [3, 5, 7, 9]
        p = 6
        q = 8

        sherlock_mini_max = SherlockMiniMax()

        self.assertEqual(6, sherlock_mini_max.get_sherlock_mini_max_2(arr, p, q))

    def test_sherlock_minimax_2(self):
        arr = [5, 8, 14]
        p = 4
        q = 9

        sherlock_mini_max = SherlockMiniMax()

        self.assertEqual(4, sherlock_mini_max.get_sherlock_mini_max_2(arr, p, q))

    def test_sherlock_minimax_3(self):
        arr = [3, 24, 35, 6, 7, 45]
        p = 15
        q = 20

        sherlock_mini_max = SherlockMiniMax()

        self.assertEqual(15, sherlock_mini_max.get_sherlock_mini_max_2(arr, p, q))

    def test_sherlock_minimax_4(self):
        arr = [263044060, 323471968, 60083128, 764550014, 209332334, 735326740, 558683912, 626871620, 232673588,
               428805364, 221674872, 261029278, 139767646, 146996700, 200921412, 121542678, 96223500, 239197414,
               407346706, 143348970, 60722446, 664904326, 352123022, 291011666, 594294166, 397870656, 60694236,
               376586636, 486260888, 114933906, 493037208, 5321608, 90019990, 601686988, 712093982, 575851770,
               411329684, 462785470, 563110618, 232790384, 511246848, 521904074, 550301294, 142371172, 241067834,
               14042944, 249208926, 36834004, 69321106, 467588012, 92173320, 360474676, 221615472, 340320496, 62541478,
               360772498, 372355942, 445408968, 342087972, 685617022, 307398890, 437939090, 720057720, 718957462,
               387059594, 583359512, 589920332, 500463226, 770726204, 434976772, 567860154, 510626506, 614077600,
               620953322, 570332092, 623026436, 502427638, 640333172, 370673998]
        p = 70283784
        q = 302962359

        sherlock_mini_max = SherlockMiniMax()

        self.assertEqual(173959056, sherlock_mini_max.get_sherlock_mini_max_2(arr, p, q))

    def test_sherlock_minimax_5(self):
        arr = [114, 48, 86, 180, 176, 66, 126, 194, 50, 198, 140, 192, 186, 4, 136, 138, 130, 178, 36, 14]

        p = 43
        q = 110

        sherlock_mini_max = SherlockMiniMax()

        self.assertEqual(100, sherlock_mini_max.get_sherlock_mini_max_2(arr, p, q))
