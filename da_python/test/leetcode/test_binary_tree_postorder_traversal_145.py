import pytest

from src.common.tree import list_to_tree
from src.leetcode.binary_tree_postorder_traversal_145 import postorder_traversal


@pytest.mark.parametrize(
    "tree_values, expected",
    [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
        ([], []),
        ([1], [1]),
    ],
)
def test_postorder_traversal(tree_values: list[int | None], expected: list[int]):
    root = list_to_tree(tree_values)
    assert postorder_traversal(root) == expected
