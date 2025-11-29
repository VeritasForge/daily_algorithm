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
    # return dfs_with_recursion(root)
    # return def_with_stack(root)
    return bfs(root)


def dfs_with_recursion(root: TreeNode | None) -> int:
    if root is None:
        return 0

    return max(dfs_with_recursion(root.left), dfs_with_recursion(root.right)) + 1


def def_with_stack(root: TreeNode | None) -> int:
    if root is None:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node is not None:
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

    return max_depth


def bfs(root: TreeNode | None) -> int:
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
