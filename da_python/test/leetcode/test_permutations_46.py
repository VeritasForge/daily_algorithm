import pytest

from src.leetcode.permutations_46 import permute


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_permute(nums: list[int], expected: list[list[int]]) -> None:
    result = permute(nums)
    assert sorted(result) == sorted(expected)
