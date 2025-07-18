import pytest

from src.leetcode.roman_to_integer_13 import roman_to_integer


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("LVIII", 58),
        ("MCI", 1_101),
        ("MCMXCIV", 1_994),
    ],
)
def test_roman_to_integer(s, expected):
    assert roman_to_integer(s) == expected
