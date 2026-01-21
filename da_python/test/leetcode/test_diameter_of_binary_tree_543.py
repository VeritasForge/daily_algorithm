import pytest

from src.common.tree import list_to_tree
from src.leetcode.diameter_of_binary_tree_543 import diameter_of_binary_tree


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ],
)
def test_diameter_of_binary_tree(nodes, expected):
    root = list_to_tree(nodes)
    assert diameter_of_binary_tree(root) == expected
