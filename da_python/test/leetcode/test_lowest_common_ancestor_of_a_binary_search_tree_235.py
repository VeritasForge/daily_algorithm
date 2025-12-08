import pytest
from src.leetcode.lowest_common_ancestor_of_a_binary_search_tree_235 import (
    lowest_common_ancestor,
)
from src.common.tree import find_node, list_to_tree


@pytest.mark.parametrize(
    "root_list, p_val, q_val, expected_lca_val",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 4, 7, 6),
        ([2, 1], 2, 1, 2),
    ],
)
def test_lowest_common_ancestor(
    root_list: list[int | None], p_val: int, q_val: int, expected_lca_val: int
):
    root = list_to_tree(root_list)
    p_node = find_node(root, p_val)
    q_node = find_node(root, q_val)

    assert root is not None and p_node is not None and q_node is not None, (
        "p or q node not found in the tree"
    )

    result_node = lowest_common_ancestor(root, p_node, q_node)
    assert result_node is not None
    assert result_node.val == expected_lca_val
