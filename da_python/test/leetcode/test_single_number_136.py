import pytest
from src.leetcode.single_number_136 import single_number


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_single_number(nums, expected):
    assert single_number(nums) == expected
