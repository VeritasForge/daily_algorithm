import pytest

from src.leetcode.maximum_subarray_53 import max_sub_array


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_max_sub_array(nums: list[int], expected: int) -> None:
    assert max_sub_array(nums) == expected
