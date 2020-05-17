import pytest
from miscelleneous.fibonacci_series import fibonacci_series, fibonacci_series_recursive, fibonacci_recursive_value


@pytest.mark.parametrize("n, expected", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (6, [0, 1, 1, 2, 3, 5]),
    (7, [0, 1, 1, 2, 3, 5, 8])
])
def test_fibonacci_series(n, expected):
    assert expected == fibonacci_series(n)


@pytest.mark.parametrize("n, expected", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (6, [0, 1, 1, 2, 3, 5]),
    (7, [0, 1, 1, 2, 3, 5, 8])
])
def test_fibonacci_series_recursive(n, expected):
    assert expected == fibonacci_series_recursive(n)


@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34)
])
def test_fibonacci_series_value(n, expected):
    assert expected == fibonacci_recursive_value(n)
