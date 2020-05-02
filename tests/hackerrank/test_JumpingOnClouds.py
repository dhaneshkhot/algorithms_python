import pytest
from algorithms.hacker_rank.JumpingOnClouds import JumpingOnClouds


@pytest.fixture(scope="module")
def jumping_on_clouds():
    return JumpingOnClouds()


@pytest.mark.parametrize("A, expected", [
    ([0, 1, 0, 0, 0, 1, 0], 3),
    ([0, 1], 1)
])
def test_jumps(jumping_on_clouds, A, expected):
    assert expected == jumping_on_clouds.count_jumps(A)
