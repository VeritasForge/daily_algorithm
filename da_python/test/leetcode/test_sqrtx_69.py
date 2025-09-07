import pytest
from src.leetcode.sqrtx_69 import my_sqrt


@pytest.mark.parametrize(
    "x, expected",
    [
        (4, 2),
        (8, 2),
        (0, 0),
        (1, 1),
    ],
)
def test_my_sqrt(x: int, expected: int):
    assert my_sqrt(x) == expected
