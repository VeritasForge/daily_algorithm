import pytest

from src.common.tree import list_to_tree
from src.leetcode.binary_tree_inorder_traversal_94 import inorder_traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_inorder_traversal(root: list[int | None], expected: list[int]):
    tree = list_to_tree(root)
    assert inorder_traversal(tree) == expected
