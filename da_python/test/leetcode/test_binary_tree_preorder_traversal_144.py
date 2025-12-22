import pytest

from src.common.tree import list_to_tree
from src.leetcode.binary_tree_preorder_traversal_144 import preorder_traversal


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([1, None, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
    ],
)
def test_preorder_traversal(tree_list: list[int | None], expected: list[int]):
    root = list_to_tree(tree_list)
    assert preorder_traversal(root) == expected
