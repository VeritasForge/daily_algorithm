import pytest
from src.leetcode.max_sub_array_content import get_max_sub_array_content


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),  # 일반적인 케이스
        ([1], [1]),  # 원소가 하나인 경우
        ([5, 4, -1, 7, 8], [5, 4, -1, 7, 8]),  # 전체가 최대인 경우
        ([-1, -2, -3], [-1]),  # 모두 음수인 경우 (가장 큰 음수 하나가 정답)
        ([1, 2, 3, -10, 4, 5], [4, 5]),  # 중간에 큰 음수가 끊어먹는 경우
    ],
)
def test_max_sub_array_content(nums: list[int], expected: list[int]):
    assert get_max_sub_array_content(nums) == expected
