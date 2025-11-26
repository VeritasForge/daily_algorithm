from __future__ import annotations
from collections import deque
from src.common.tree import TreeNode


"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    q = deque([root])
    dept = 0

    while q:
        dept += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return dept
