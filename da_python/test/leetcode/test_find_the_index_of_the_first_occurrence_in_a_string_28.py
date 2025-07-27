import pytest

from src.leetcode.find_the_index_of_the_first_occurrence_in_a_string_28 import to_string


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
    ],
)
def test_find_the_index_of_the_first_occurrence_in_a_string(
    haystack: str, needle: str, expected: int
):
    assert to_string(haystack, needle) == expected
