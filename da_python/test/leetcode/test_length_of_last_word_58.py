import pytest
from src.leetcode.length_of_last_word_58 import length_of_last_word


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("   Hello", 5),
        ("Hello", 5),
    ],
)
def test_length_of_last_word(s, expected):
    assert length_of_last_word(s) == expected
