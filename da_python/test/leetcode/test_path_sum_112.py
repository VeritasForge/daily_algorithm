import pytest

from src.common.tree import list_to_tree
from src.leetcode.path_sum_112 import has_path_sum


@pytest.mark.parametrize(
    "values, target_sum, expected",
    [
        # LeetCode 기본 예제
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
        # # 보강 - 엣지 케이스
        ([1], 1, True),
        ([1], 0, False),
        # 보강 - 예외 케이스 (음수 값 포함)
        ([-2, None, -3], -5, True),
        # target_sum=0은 falsy 값이므로 "타겟 없음"으로 오판하기 쉬운 함정 케이스
        ([1, -2, -3, 1, 3, -2, None], 0, True),
        # 보강 - 추가 검증 (한쪽으로 치우친 트리)
        ([1, 2], 1, False),
        ([2, 3, None, 4, None, 5], 14, True),
    ],
)
def test_has_path_sum(values: list[int | None], target_sum: int, expected: bool):
    root = list_to_tree(values)
    assert has_path_sum(root, target_sum) == expected
