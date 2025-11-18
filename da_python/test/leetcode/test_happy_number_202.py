import pytest
from src.leetcode.happy_number_202 import is_happy


@pytest.mark.parametrize(
    "n, expected",
    [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
    ],
)
def test_is_happy(n: int, expected: bool):
    assert is_happy(n) == expected
