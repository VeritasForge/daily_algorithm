import pytest

from src.leetcode.remove_element_27 import remove_element


@pytest.mark.parametrize(
    "nums, val, expected",
    [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([2, 2, 3, 3], 3, [2, 2]),
        ([3, 3, 2, 2], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([2], 3, [2]),
        ([3], 3, []),
        ([3, 3], 5, [3, 3]),
    ],
)
def test_remove_element(nums, val, expected):
    assert remove_element(nums, val) == len(expected)
    assert nums[: len(expected)] == expected
