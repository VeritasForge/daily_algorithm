import pytest

from src.leetcode.valid_anagram_242 import is_anagram


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("ab", "abc", False),
        ("한국어", "어국한", True),
        ("한국", "어국한", False),
    ],
)
def test_is_anagram(s: str, t: str, expected: bool):
    assert is_anagram(s, t) == expected
