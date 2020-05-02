import pytest
from miscelleneous.sum_of_2_elements_16 import get_list_of_tuples_from_list_for_which_sum_is_16


@pytest.mark.parametrize("a, expected", [
    ([1, 4, 45, 6, 10, -8], [(6, 10)]),
    ([1, -26, 4, 45, 6, 10, -8, 42], [(-26, 42), (6, 10)])
])
def test_sum_in_list_16(a, expected):
    b = 16
    t = get_list_of_tuples_from_list_for_which_sum_is_16(a, b)
    assert expected == t
