import unittest
from algorithms.codility_tests.OddOccurrencesInArray import OddOccurrencesInArray


class CyclicRotationTests(unittest.TestCase):

    def test_odd_occurance(self):
        A = [9, 3, 9, 3, 9, 7, 9]
        odd_occurances = OddOccurrencesInArray()
        self.assertEqual(7, odd_occurances.odd_occurances_in_array(A))

    def test_odd_occurance2(self):
        A = [9, 3, 9, 3, 9, 7, 9]
        odd_occurances = OddOccurrencesInArray()
        self.assertEqual(7, odd_occurances.odd_occurances_in_array_2(A))


if __name__ == '__main__':
    unittest.main()