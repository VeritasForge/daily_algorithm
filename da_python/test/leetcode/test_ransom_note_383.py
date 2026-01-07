import pytest

from src.leetcode.ransom_note_383 import can_construct


@pytest.mark.parametrize(
    "ransom_note, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("aab", "baa", True),
    ],
)
def test_can_construct(ransom_note: str, magazine: str, expected: bool) -> None:
    assert can_construct(ransom_note, magazine) == expected
