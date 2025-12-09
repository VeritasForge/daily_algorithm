# https://leetcode.com/problems/same-tree/
# 100. Same Tree
#
# Given the roots of two binary trees p and q, write a function to check
# if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
# Example 1:
#   Input: p = [1,2,3], q = [1,2,3]
#   Output: true
#
# Example 2:
#   Input: p = [1,2], q = [1,null,2]
#   Output: false
#
# Example 3:
#   Input: p = [1,2,1], q = [1,1,2]
#   Output: false
#
# Constraints:
#   - The number of nodes in both trees is in the range [0, 100].
#   - -10^4 <= Node.val <= 10^4

from collections import deque

from src.common.tree import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # return _bfs(p, q)
    # return _dfs(p, q)
    return _dfs_stack(p, q)


def _bfs(p: TreeNode | None, q: TreeNode | None) -> bool:
    queue = deque([(p, q)])

    while queue:
        first, second = queue.pop()

        if first is None and second is None:
            continue

        if (first is None or second is None) or (first.val != second.val):
            return False

        queue.append((first.left, second.left))
        queue.append((first.right, second.right))

    return True


def _dfs(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return p.val == q.val and _dfs(p.left, q.left) and _dfs(p.right, q.right)


def _dfs_stack(p: TreeNode | None, q: TreeNode | None) -> bool:
    stack = [(p, q)]

    while stack:
        first, second = stack.pop()

        if first is None and second is None:
            continue

        if (first is None or second is None) or (first.val != second.val):
            return False

        stack.append((first.right, second.right))
        stack.append((first.left, second.left))

    return True
