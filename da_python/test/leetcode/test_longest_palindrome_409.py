import pytest

from src.leetcode.longest_palindrome_409 import longest_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abccccdd", 7),
        ("a", 1),
        ("bb", 2),
    ],
)
def test_longest_palindrome(s: str, expected: int):
    assert longest_palindrome(s) == expected
