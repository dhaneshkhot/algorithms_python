import pytest
from algorithms.ds.sorting.QuickSort import quick_sort


@pytest.mark.parametrize("arr, expected", [
    ([3, 8, 9, 7, 6], [3, 6, 7, 8, 9]),
    ([3, 8, 9, 3, 2, -4, -8, -100, 100, 7, 6], [-100, -8, -4, 2, 3, 3, 6, 7, 8, 9, 100]),
])
def test_quick_sort(arr, expected):
    assert expected == quick_sort(arr)

