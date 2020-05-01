import unittest
from miscelleneous.CreditCardNoCheck import CreditCardNoCheck


class TestsCreditCardNoCheck(unittest.TestCase):

    def test_check_if_valid_card_no_1(self):
        c = CreditCardNoCheck()
        self.assertEqual(True, c.check_if_valid_card_no("4123456789123456"))

    def test_check_if_valid_card_no_2(self):
        c = CreditCardNoCheck()
        self.assertEqual(True, c.check_if_valid_card_no("5123-4567-8912-3456"))

    def test_check_if_valid_card_no_3(self):
        c = CreditCardNoCheck()
        self.assertEqual(False, c.check_if_valid_card_no("61234-567-8912-3456"))

    def test_check_if_valid_card_no_4(self):
        c = CreditCardNoCheck()
        self.assertEqual(True, c.check_if_valid_card_no("4123356789123456"))

    def test_check_if_valid_card_no_5(self):
        c = CreditCardNoCheck()
        self.assertEqual(False, c.check_if_valid_card_no("5133-3367-8912-3456"))

    def test_check_if_valid_card_no_6(self):
        c = CreditCardNoCheck()
        self.assertEqual(False, c.check_if_valid_card_no("5123 - 3567 - 8912 - 3456"))


if __name__ == '__main__':
    unittest.main()
