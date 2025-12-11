import pytest

from src.common.tree import tree_to_list
from src.leetcode.convert_sorted_array_to_binary_search_tree_108 import (
    sorted_array_to_bst,
)


# def is_balanced(root: TreeNode | None) -> bool:
#     """Check if tree is height-balanced."""
#
#     def height(node: TreeNode | None) -> int:
#         if not node:
#             return 0
#         left_h = height(node.left)
#         right_h = height(node.right)
#         if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
#             return -1
#         return max(left_h, right_h) + 1
#
#     return height(root) != -1
#
#
# def is_valid_bst(root: TreeNode | None) -> bool:
#     """Check if tree is a valid BST."""
#
#     def validate(node: TreeNode | None, min_val: float, max_val: float) -> bool:
#         if not node:
#             return True
#         if not (min_val < node.val < max_val):
#             return False
#         return validate(node.left, min_val, node.val) and validate(
#             node.right, node.val, max_val
#         )
#
#     return validate(root, float("-inf"), float("inf"))
#
#
# def inorder_traversal(root: TreeNode | None) -> list[int]:
#     """Get inorder traversal of tree."""
#     result: list[int] = []
#
#     def inorder(node: TreeNode | None) -> None:
#         if node:
#             inorder(node.left)
#             result.append(node.val)
#             inorder(node.right)
#
#     inorder(root)
#     return result


@pytest.mark.parametrize(
    "nums, exp",
    [
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
        ([1, 3], [3, 1]),
        ([1], [1]),
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 6, 1, 3, 5, 7]),
    ],
)
def test_sorted_array_to_bst(nums: list[int], exp: list[int]) -> None:
    assert tree_to_list(sorted_array_to_bst(nums)) == exp
