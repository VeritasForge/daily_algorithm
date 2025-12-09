import pytest

from src.common.tree import list_to_tree
from src.leetcode.same_tree_100 import is_same_tree


@pytest.mark.parametrize(
    "p, q, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_is_same_tree(p: list[int | None], q: list[int | None], expected: bool):
    tree_p = list_to_tree(p)
    tree_q = list_to_tree(q)
    assert is_same_tree(tree_p, tree_q) == expected
