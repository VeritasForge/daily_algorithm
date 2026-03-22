# https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
# Example 1:
#     Input: root = [1,2,2,3,4,4,3]
#     Output: true
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3
#
# Example 2:
#     Input: root = [1,2,2,null,3,null,3]
#     Output: false
#         1
#        / \
#       2   2
#        \   \
#        3    3
#
# Constraints:
#     - The number of nodes in the tree is in the range [1, 1000].
#     - -100 <= Node.val <= 100

from src.common.tree import TreeNode


# BFS
# def is_symmetric(root: TreeNode | None) -> bool:
#     q = deque([(root.left, root.right)])
#     while q:
#         left, right = q.popleft()
#         if left is None and right is None:
#             continue
#
#         if left is None or right is None or left.val != right.val:
#             return False
#
#         q.append((left.left, right.right))
#         q.append((left.right, right.left))
#
#     return True

# Iterative DFS
# def is_symmetric(root: TreeNode | None) -> bool:
#     stack = [(root.left, root.right)]
#
#     while stack:
#         left, right = stack.pop()
#         if left is None and right is None:
#             continue
#
#         if left is None or right is None or left.val != right.val:
#             return False
#
#         stack.append((left.left, right.right))
#         stack.append((left.right, right.left))


# Recursive DFS
def is_symmetric(root: TreeNode | None) -> bool:
    def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return (
            left.val == right.val
            and is_mirror(left.left, right.right)
            and is_mirror(left.right, right.left)
        )

    return root is None or is_mirror(root.left, root.right)
