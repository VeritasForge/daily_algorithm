import pytest

from src.leetcode.longest_palindromic_substring_5 import longest_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", ["bab", "aba"]),  # 두 답 모두 유효
        ("cbbd", ["bb"]),
    ],
)
def test_longest_palindrome(s: str, expected: list[str]):
    result = longest_palindrome(s)
    assert result in expected
