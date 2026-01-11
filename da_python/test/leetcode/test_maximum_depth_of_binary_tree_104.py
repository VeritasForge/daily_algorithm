import pytest

from src.common.tree import list_to_tree
from src.leetcode.maximum_depth_of_binary_tree_104 import max_depth


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([0], 1),
        ([1, 2, 3, 4, None, None, 5], 3),
    ],
)
def test_max_depth(nodes, expected):
    root = list_to_tree(nodes)
    assert max_depth(root) == expected
