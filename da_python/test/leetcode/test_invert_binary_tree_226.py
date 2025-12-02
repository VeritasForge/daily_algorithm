import pytest

from src.common.tree import list_to_tree, tree_to_list
from src.leetcode.invert_binary_tree_226 import invert_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_tree(root: list[int | None], expected: list[int | None]):
    tree = list_to_tree(root)
    result = invert_tree(tree)
    assert tree_to_list(result) == expected
