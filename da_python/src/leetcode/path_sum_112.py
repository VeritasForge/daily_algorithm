# https://leetcode.com/problems/path-sum/
# 112. Path Sum
#
# Given the root of a binary tree and an integer targetSum, return true
# if the tree has a root-to-leaf path such that adding up all the values
# along the path equals targetSum.
#
# A leaf is a node with no children.
#
# Example 1:
#   Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: true
#
# Example 2:
#   Input: root = [1,2,3], targetSum = 5
#   Output: false
#
# Example 3:
#   Input: root = [], targetSum = 0
#   Output: false
#
# Constraints:
#   - The number of nodes in the tree is in the range [0, 5000].
#   - -1000 <= Node.val <= 1000
#   - -1000 <= targetSum <= 1000
from src.common.tree import TreeNode


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if root is None:
        return False

    stack = [(root, target_sum)]
    while stack:
        curr, remaining = stack.pop()
        remaining -= curr.val or 0

        if curr.left is None and curr.right is None and remaining == 0:
            return True

        if curr.right is not None:
            stack.append((curr.right, remaining))
        if curr.left is not None:
            stack.append((curr.left, remaining))

    return False


# def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
#     if root is None:
#         return False

#     remaining = target_sum - (0 if root.val is None else root.val)

#     if root.left is None and root.right is None:
#         return remaining == 0

#     return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)
