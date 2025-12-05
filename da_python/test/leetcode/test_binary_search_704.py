import pytest

from src.leetcode.binary_search_704 import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_search(nums: list[int], target: int, expected: int) -> None:
    assert search(nums, target) == expected
