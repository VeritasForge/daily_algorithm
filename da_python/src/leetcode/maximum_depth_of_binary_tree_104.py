from __future__ import annotations
from collections import deque
from src.common.tree import TreeNode


"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# def max_depth(root: TreeNode | None) -> int:
#     if root is None:
#         return 0
#
#     return max(max_depth(root.left), max_depth(root.right)) + 1


# def max_depth(root: TreeNode | None) -> int:
#     stack, max_depth = [(root, 1)], 0
#     while stack:
#         curr, depth = stack.pop()
#         if curr is None:
#             continue
#
#         max_depth = max(depth, max_depth)
#
#         stack.append((curr.left, max_depth + 1))
#         stack.append((curr.right, max_depth + 1))
#
#     return max_depth


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    q, depth = deque([root]), 0

    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return depth
