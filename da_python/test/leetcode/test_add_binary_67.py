import pytest
from src.leetcode.add_binary_67 import add_binary


@pytest.mark.parametrize(
    "a, b, expected",
    [("11", "1", "100"), ("1010", "1011", "10101")],
)
def test_add_binary(a: str, b: str, expected: str):
    assert add_binary(a, b) == expected
