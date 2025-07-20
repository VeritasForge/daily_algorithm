import pytest

from src.leetcode.valid_paretheses_20 import is_valid


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("(]", False),
        ("([)]", False),
        ("]", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) is expected
