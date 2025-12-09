import pytest

from src.common.tree import list_to_tree
from src.leetcode.balanced_binary_tree_110 import is_balanced


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
    ],
)
def test_is_balanced(tree_list: list[int | None], expected: bool):
    root = list_to_tree(tree_list)
    assert is_balanced(root) == expected
