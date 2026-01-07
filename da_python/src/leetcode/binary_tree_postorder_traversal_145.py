# https://leetcode.com/problems/binary-tree-postorder-traversal/
# 145. Binary Tree Postorder Traversal
#
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# Postorder traversal visits nodes in the order: left -> right -> root
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

from src.common.tree import TreeNode


# def postorder_traversal(root: TreeNode | None) -> list[int | None]:
#     result: list[int | None] = []
#
#     def recursive(node: TreeNode | None):
#         if node is None:
#             return
#
#         recursive(node.left)
#         recursive(node.right)
#
#         result.append(node.val)
#
#     recursive(root)
#     return result


# def postorder_traversal(root: TreeNode | None) -> list[int | None]:
#     if root is None:
#         return []
#
#     return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


# def postorder_traversal(root: TreeNode | None) -> list[int | None]:
#     result: list[int | None] = []
#     stack: list[TreeNode | None] = [root]
#
#     while stack:
#         node = stack.pop()
#         if node is None:
#             continue
#
#         result.append(node.val)
#
#         stack.append(node.left)
#         stack.append(node.right)
#
#     return result[::-1]


def postorder_traversal(root: TreeNode | None) -> list[int | None]:
    res, stack = [], []
    curr, prev = root, None

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack[-1]

        if curr.right is None or curr.right == prev:
            res.append(curr.val)
            stack.pop()
            prev = curr
            curr = None
        else:
            curr = curr.right

    return res
