import pytest

from src.common.tree import list_to_tree
from src.leetcode.minimum_depth_of_binary_tree_111 import min_depth


@pytest.mark.parametrize(
    "values, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([], 0),
    ],
)
def test_min_depth(values: list[int | None], expected: int):
    root = list_to_tree(values)
    assert min_depth(root) == expected
