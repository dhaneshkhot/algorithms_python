from miscelleneous.CreditCardNoCheck import CreditCardNoCheck
import pytest


@pytest.fixture(scope="module")
def setup():
    yield CreditCardNoCheck()


@pytest.mark.parametrize("input_value, expected_value", [
    ('4123456789123456', True),
    ('5123-4567-8912-3456', True),
    ('61234-567-8912-3456', False),
    ('4123356789123456', True),
    ('5133-3367-8912-3456', False),
    ('5123 - 3567 - 8912 - 3456', False)
])
def test_check_if_valid_card_no(setup, input_value, expected_value):
    actual_value = setup.check_if_valid_card_no(input_value)
    assert actual_value == expected_value
