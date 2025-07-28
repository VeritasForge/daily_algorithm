import pytest

from src.leetcode.search_insert_position_35 import search_insert


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_search_insert(nums: list[int], target: int, expected: int):
    assert search_insert(nums, target) == expected
