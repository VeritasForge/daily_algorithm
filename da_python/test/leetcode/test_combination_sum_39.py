import pytest

from src.leetcode.combination_sum_39 import combination_sum


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([7, 2, 3], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ],
)
def test_combination_sum(
    candidates: list[int], target: int, expected: list[list[int]]
) -> None:
    result = combination_sum(candidates, target)
    # 순서에 상관없이 비교하기 위해 정렬 후 비교
    assert sorted([sorted(combo) for combo in result]) == sorted(
        [sorted(combo) for combo in expected]
    )
