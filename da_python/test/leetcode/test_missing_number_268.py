import pytest

from src.leetcode.missing_number_268 import missing_number


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test_missing_number(nums: list[int], expected: int):
    assert missing_number(nums) == expected
