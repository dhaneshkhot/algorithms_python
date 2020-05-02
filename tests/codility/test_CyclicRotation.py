import pytest
from algorithms.codility_tests.CyclicRotation import CyclicRotation


@pytest.fixture(scope="module")
def cyclic_rotation():
    return CyclicRotation()


@pytest.mark.parametrize("A, expected", [
    ([3, 8, 9, 7, 6], [9, 7, 6, 3, 8]),
    ([3], [3])
])
def test_cyclic_rotation(cyclic_rotation, A, expected):
    K = 3
    assert expected == cyclic_rotation.cyclic_rotate_array(A, K)
