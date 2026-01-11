import pytest

from src.leetcode.longest_substring_without_repeating_characters_3 import (
    length_of_longest_substring,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        # Example 1: "abc"가 가장 긴 중복 없는 부분 문자열
        ("abcabcbb", 3),
        # Example 2: 모든 문자가 같으므로 "b" 하나만 가능
        ("bbbbb", 1),
        # Example 3: "wke"가 가장 긴 중복 없는 부분 문자열
        ("pwwkew", 3),
        # Edge case: 빈 문자열
        ("", 0),
        # Edge case: 한 글자
        ("a", 1),
        # 공백 포함
        (" ", 1),
        # 모든 문자가 고유한 경우
        ("abcdef", 6),
    ],
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    assert length_of_longest_substring(s) == expected
