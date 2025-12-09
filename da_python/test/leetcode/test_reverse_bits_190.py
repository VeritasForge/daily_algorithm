import pytest

from src.leetcode.reverse_bits_190 import reverse_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (0b00000010100101000001111010011100, 964176192),
        (0b11111111111111111111111111111101, 3221225471),
    ],
)
def test_reverse_bits(n: int, expected: int):
    assert reverse_bits(n) == expected
