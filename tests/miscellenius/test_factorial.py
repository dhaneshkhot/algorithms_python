import pytest
from miscelleneous.factorial import factorial


@pytest.mark.parametrize("n, expected", [
    (5, 120),
    (4, 24),
    (7, 5040)
])
def test_factorial(n, expected):
    assert expected == factorial(n)
