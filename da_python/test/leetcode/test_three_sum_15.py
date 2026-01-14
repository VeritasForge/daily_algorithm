import pytest

from src.leetcode.three_sum_15 import three_sum


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-100, -70, -60, 110, 120, 130, 160], [[-100, -60, 160], [-70, -60, 130]]),
    ],
)
def test_three_sum(nums: list[int], expected: list[list[int]]):
    result = three_sum(nums)
    # 순서에 관계없이 비교하기 위해 정렬 후 비교
    assert sorted([sorted(triplet) for triplet in result]) == sorted(
        [sorted(triplet) for triplet in expected]
    )
