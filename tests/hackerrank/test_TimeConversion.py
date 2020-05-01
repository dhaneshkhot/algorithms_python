import unittest
from algorithms.hacker_rank.TimeConversion import TimeConversion


class TestsTimeConversion(unittest.TestCase):

    def test_time_conversion_1(self):
        input_time = "07:05:45PM"
        time_conversion = TimeConversion()
        self.assertEqual("19:05:45", time_conversion.time_conversion(input_time))

    def test_time_conversion_2(self):
        input_time = "07:05:45AM"
        time_conversion = TimeConversion()
        self.assertEqual("07:05:45", time_conversion.time_conversion(input_time))

    def test_time_conversion_3(self):
        input_time = "12:05:45AM"
        time_conversion = TimeConversion()
        self.assertEqual("00:05:45", time_conversion.time_conversion(input_time))

    def test_time_conversion_4(self):
        input_time = "12:05:45PM"
        time_conversion = TimeConversion()
        self.assertEqual("12:05:45", time_conversion.time_conversion(input_time))


if __name__ == '__main__':
    unittest.main()
