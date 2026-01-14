import pytest

from src.leetcode.search_in_rotated_sorted_array_33 import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ],
)
def test_search(nums: list[int], target: int, expected: int) -> None:
    assert search(nums, target) == expected
