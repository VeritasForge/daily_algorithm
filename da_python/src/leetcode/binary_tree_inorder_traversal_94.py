# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal
#
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [1,3,2]
#
# Example 2:
#   Input: root = []
#   Output: []
#
# Example 3:
#   Input: root = [1]
#   Output: [1]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

from src.common.tree import TreeNode


# def inorder_traversal(root: TreeNode | None) -> list[int | None]:
#     result: list[int | None] = []
#
#     def recursion(node: TreeNode | None):
#         if node is None:
#             return
#
#         recursion(node.left)
#         result.append(node.val)
#         recursion(node.right)
#
#     recursion(root)
#     return result


# def inorder_traversal(root: TreeNode | None) -> list[int | None]:
#     if root is None:
#         return []
#
#     return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def inorder_traversal(root: TreeNode | None) -> list[int | None]:
    result: list[int | None] = []
    stack: list[TreeNode] = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.val)

        curr = curr.right

    return result
