import pytest
from src.leetcode.maximum_product_subarray_152 import max_product


@pytest.mark.skip(reason="구현 미완성 (TODO)")
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, -2, 4], 6),  # [2, 3]의 곱 6
        ([-2, 0, -1], 0),  # 0이 포함된 경우
        ([-2, 3, -4], 24),  # 음수와 음수가 만나 양수가 되는 경우 (중요!)
        ([0, 2], 2),  # 0 뒤에 양수가 오는 경우
        ([-1, -2, -3], 6),  # 음수 세 개
        ([2, -5, -2, -4, 3], 24),  # 복합 케이스
    ],
)
def test_max_product(nums: list[int], expected: int):
    assert max_product(nums) == expected
