import pytest

from src.leetcode.letter_combinations_of_a_phone_number_17 import letter_combinations


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
    ],
)
def test_letter_combinations(digits: str, expected: list[str]):
    result = letter_combinations(digits)
    assert sorted(result) == sorted(expected)
