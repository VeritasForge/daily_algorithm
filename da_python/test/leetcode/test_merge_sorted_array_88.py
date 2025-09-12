import pytest
from src.leetcode.merge_sorted_array_88 import merge


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1, 4, 5, 0, 0, 0], 3, [2, 3, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([2, 4, 5, 0, 0, 0], 3, [1, 3, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge(nums1: list[int], m: int, nums2: list[int], n: int, expected: list[int]):
    merge(nums1, m, nums2, n)
    assert nums1 == expected
