import pytest

from src.common.tree import list_to_tree
from src.leetcode.count_complete_tree_nodes_222 import count_nodes


@pytest.mark.parametrize(
    "values, expected",
    [
        # LeetCode 기본 예제
        ([1, 2, 3, 4, 5, 6], 6),
        ([], 0),
        ([1], 1),
        # 보강 - 엣지 케이스 (마지막 레벨에 노드가 1개만 있는 경우)
        ([1, 2, 3, 4], 4),
        ([1, 2], 2),
        # 보강 - 예외 케이스 (완전 이진 트리의 마지막 레벨이 꽉 찬 경우, perfect binary tree)
        ([1, 2, 3, 4, 5, 6, 7], 7),
        # 보강 - 추가 검증 (더 깊은 트리, 마지막 레벨이 일부만 채워진 경우)
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15),
    ],
)
def test_count_nodes(values: list[int | None], expected: int):
    root = list_to_tree(values)
    assert count_nodes(root) == expected
