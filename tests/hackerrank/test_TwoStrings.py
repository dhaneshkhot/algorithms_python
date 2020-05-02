import pytest
from algorithms.hacker_rank.TwoStrings import TwoStrings


@pytest.fixture(scope="module")
def two_strings():
    return TwoStrings()


@pytest.mark.parametrize("s1, s2, expected", [
    ("hello", "world", "YES"),
    ("hi", "world", "NO")
])
def test_do_they_share_common_substring_1(two_strings, s1, s2, expected):
    assert expected == two_strings.do_they_share_common_substring_1(s1, s2)


@pytest.mark.parametrize("s1, s2, expected", [
    ("hello", "world", "YES"),
    ("hi", "world", "NO")
])
def test_do_they_share_common_substring_2(two_strings, s1, s2, expected):
    assert expected == two_strings.do_they_share_common_substring_2(s1, s2)


@pytest.mark.parametrize("s1, s2, expected", [
    ("hello", "world", "YES"),
    ("hi", "world", "NO")
])
def test_do_they_share_common_substring_3(two_strings, s1, s2, expected):
    assert expected == two_strings.do_they_share_common_substring_3(s1, s2)
