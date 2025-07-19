import pytest

from src.leetcode.longest_common_prefix_14 import longest_common_prefix


@pytest.mark.parametrize(
    "strs, expected",
    (
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["cir", "car"], "c"),
    ),
)
def test_longest_common_prefix(strs: list[str], expected: str):
    assert longest_common_prefix(strs) == expected
