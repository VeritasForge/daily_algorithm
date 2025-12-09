import pytest

from src.leetcode.majority_element_169 import majority_element


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ],
)
def test_majority_element(nums: list[int], expected: int):
    assert majority_element(nums) == expected
