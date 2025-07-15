import pytest

from src.leetcode.palindrome_number_9 import is_palindrome


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (0, True),
        (-121, False),
        (10, False),
    ],
)
def test_palindrom_number(x, expected):
    assert is_palindrome(x) is expected
