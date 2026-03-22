import pytest

from src.common.tree import list_to_tree
from src.leetcode.symmetric_tree_101 import is_symmetric


@pytest.mark.parametrize(
    "values, expected",
    [
        # 기본 예제
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        # 노드 1개 (root만)
        ([1], True),
        # 값은 같지만 위치가 비대칭
        ([1, 2, 2, None, 3, 3, None], True),
        ([1, 2, 2, 3, None, None, 3], True),
        ([1, 2, 2, 3, None, 3, None], False),
        # 왼쪽/오른쪽 값 자체가 다름
        ([1, 2, 3], False),
        # 깊은 트리 대칭
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], True),
        # 깊은 트리 비대칭 (리프 하나 다름)
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 9], False),
    ],
)
def test_is_symmetric(values: list[int | None], expected: bool):
    root = list_to_tree(values)
    assert is_symmetric(root) == expected
