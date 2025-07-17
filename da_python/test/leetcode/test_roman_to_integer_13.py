import pytest

from src.leetcode.roman_to_integer_13 import roman_to_integer


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_roman_to_integer(s, expected):
    assert roman_to_integer(s) == expected
