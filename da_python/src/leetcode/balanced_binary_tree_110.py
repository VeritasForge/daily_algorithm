# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
# A height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node
# differ in height by no more than 1.
#
# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#         3
#        / \
#       9  20
#         /  \
#        15   7
#     Output: true
#
# Example 2:
#     Input: root = [1,2,2,3,3,null,null,4,4]
#           1
#          / \
#         2   2
#        / \
#       3   3
#      / \
#     4   4
#     Output: false
#
# Example 3:
#     Input: root = []
#     Output: true

from src.common.tree import TreeNode


def is_balanced(root: TreeNode | None) -> bool:
    # return _dfs(root) > -1
    return _dfs_stack(root)


def _dfs(node: TreeNode | None) -> int:
    if node is None:
        return 0

    left_height = _dfs(node.left)
    if left_height == -1:
        return -1

    right_height = _dfs(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def _dfs_stack(root: TreeNode | None) -> bool:
    if root is None:
        return True

    stack: list[TreeNode] = []
    heights: dict[int, int] = {}
    node: TreeNode | None = root
    prev = None

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack[-1]

        if node.right and node.right is not prev:
            node = node.right
            continue

        stack.pop()

        left_height = heights.get(id(node.left), 0)
        right_height = heights.get(id(node.right), 0)

        if abs(left_height - right_height) > 1:
            return False

        heights[id(node)] = max(left_height, right_height) + 1

        prev = node
        node = None

    return True
