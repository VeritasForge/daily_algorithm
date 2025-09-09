import pytest

from src.leetcode.fibonacci_number_509 import fib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (30, 832040),
    ],
)
def test_fib(n: int, expected: int):
    assert fib(n) == expected
