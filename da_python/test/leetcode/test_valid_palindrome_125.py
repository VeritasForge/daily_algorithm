import pytest

from src.leetcode.valid_palindrome_125 import is_palindrome


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("level", True),
        ("0P", False),
    ],
)
def test_is_palindrome(s: str, expected: bool):
    assert is_palindrome(s) == expected
