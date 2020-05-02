import pytest
from algorithms.hacker_rank.BinarySorting import BinarySorting, get_no_of_ones


@pytest.fixture(scope="module")
def test_binary_sorting():
    return BinarySorting()


def test_rearrange(test_binary_sorting):
    A = [7, 8, 5, 6]
    assert ['1000', '0101', '0110', '0111'] == test_binary_sorting.rearrange(A)


def test_get_no_of_ones():
    assert 4 == get_no_of_ones("1111")
