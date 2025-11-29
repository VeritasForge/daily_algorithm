# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: 2
#
# Example 2:
#   Input: root = [2,null,3,null,4,null,5,null,6]
#   Output: 5
#
# Constraints:
#   - The number of nodes in the tree is in the range [0, 10^5].
#   - -1000 <= Node.val <= 1000
import sys
from collections import deque

from src.common.tree import TreeNode


def min_depth(root: TreeNode | None) -> int:
    # return bfs(root)
    # return dfs_with_recursion(root)
    return dfs_with_stack(root)


def bfs(root: TreeNode | None) -> int:
    if root is None:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()

            if not (node.left or node.right):
                return depth

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return depth


def dfs_with_recursion(root: TreeNode | None) -> int:
    if root is None:
        return 0

    if root.left and root.right is None:
        return dfs_with_recursion(root.left) + 1

    if root.right and root.left is None:
        return dfs_with_recursion(root.right) + 1

    return min(dfs_with_recursion(root.left), dfs_with_recursion(root.right)) + 1


def dfs_with_stack(root: TreeNode | None) -> int:
    if root is None:
        return 0

    min_dep = sys.maxsize
    stack = [(root, 1)]

    while stack:
        node, depth = stack.pop()
        if min_dep <= depth:
            continue

        if not (node.left or node.right):
            min_dep = min(min_dep, depth)
            continue

        if node.right:
            stack.append((node.right, depth + 1))

        if node.left:
            stack.append((node.left, depth + 1))

    return min_dep
