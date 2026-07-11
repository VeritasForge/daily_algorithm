"""
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Difficulty: Easy

문제 설명:
    Given the root of a complete binary tree, return the number of the
    nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is
    completely filled in a complete binary tree, and all nodes in the
    last level are as far left as possible. It can have between 1 and
    2^h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.

    Example 1:

    Input: root = [1,2,3,4,5,6]
    Output: 6

    Example 2:

    Input: root = []
    Output: 0

    Example 3:

    Input: root = [1]
    Output: 1

제약 조건:
    The number of nodes in the tree is in the range [0, 5 * 10^4].
    0 <= Node.val <= 5 * 10^4
    The tree is guaranteed to be complete.
"""

# from collections import deque

from src.common.tree import TreeNode


def height(curr: TreeNode | None) -> int:
    if curr is None:
        return 0

    return 1 + height(curr.left)

def count_nodes(root: TreeNode | None) -> int:
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height == right_height:
        return (1 << left_height) + count_nodes(root.right)
    return (1 << right_height) + count_nodes(root.left)

# def count_nodes(root: TreeNode | None) -> int:
#     if root is None:
#         return 0

#     def height(curr: TreeNode | None) -> int:
#         if curr is None:
#             return 0

#         return 1 + height(curr.left)

#     l_height = height(root.left)
#     r_height = height(root.right)

#     if l_height == r_height:
#         return (1 << l_height) + count_nodes(root.right)

#     return (1 << r_height) + count_nodes(root.left)


# def count_nodes(root: TreeNode | None) -> int:
#     q, cnt = deque([root]), 0

#     while q:
#         curr = q.popleft()
#         if curr is None:
#             continue

#         cnt += 1
#         q.append(curr.left)
#         q.append(curr.right)

#     return cnt

# def count_nodes(root: TreeNode | None) -> int:
#     stack, cnt = [root], 0

#     while stack:
#         curr = stack.pop()
#         if curr is None:
#             continue

#         cnt += 1

#         stack.append(curr.right)
#         stack.append(curr.left)

#     return cnt


# def count_nodes(root: TreeNode | None) -> int:
#     if root is None:
#         return 0

#     return 1 + count_nodes(root.left) + count_nodes(root.right)
