# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# Example 1:
#   Input: root = [4,2,7,1,3,6,9]
#   Output: [4,7,2,9,6,3,1]
#
#       4               4
#      / \             / \
#     2   7    →      7   2
#    / \ / \         / \ / \
#   1  3 6  9       9  6 3  1
#
# Example 2:
#   Input: root = [2,1,3]
#   Output: [2,3,1]
#
# Example 3:
#   Input: root = []
#   Output: []
#
# Constraints:
#   - The number of nodes in the tree is in the range [0, 100].
#   - -100 <= Node.val <= 100

from collections import deque

from src.common.tree import TreeNode


# def invert_tree(root: TreeNode | None) -> TreeNode | None:
#     if root is None:
#         return
#
#     root.left, root.right = invert_tree(root.right), invert_tree(root.left)
#     return root


# def invert_tree(root: TreeNode | None) -> TreeNode | None:
#     stack = [root]
#
#     while stack:
#         curr = stack.pop()
#         if curr is None:
#             continue
#
#         curr.left, curr.right = curr.right, curr.left
#
#         stack.append(curr.right)
#         stack.append(curr.left)
#
#     return root


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    q = deque([root])

    while q:
        curr = q.popleft()
        if curr is None:
            continue

        curr.left, curr.right = curr.right, curr.left

        q.append(curr.left)
        q.append(curr.right)

    return root
