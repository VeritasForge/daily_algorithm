import pytest

from src.leetcode.power_of_three_326 import is_power_of_three


@pytest.mark.parametrize(
    "n, expected",
    [
        (27, True),
        (0, False),
        (-1, False),
    ],
)
def test_is_power_of_three(n: int, expected: bool) -> None:
    assert is_power_of_three(n) == expected
