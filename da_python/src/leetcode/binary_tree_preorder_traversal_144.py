# https://leetcode.com/problems/binary-tree-preorder-traversal/
# 144. Binary Tree Preorder Traversal
#
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Preorder traversal visits nodes in the order: root -> left -> right
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [1,2,3]
#
# Example 2:
#   Input: root = []
#   Output: []
#
# Example 3:
#   Input: root = [1]
#   Output: [1]
#
# Constraints:
#   - The number of nodes in the tree is in the range [0, 100].
#   - -100 <= Node.val <= 100
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

from src.common.tree import TreeNode


# def preorder_traversal(root: TreeNode | None) -> list[int | None]:
#     result: list[int | None] = []
#
#     def recursive(node: TreeNode | None) -> None:
#         if node is None:
#             return
#
#         result.append(node.val)
#         recursive(node.left)
#         recursive(node.right)
#
#     recursive(root)
#     return result


# def preorder_traversal(root: TreeNode | None) -> list[int | None]:
#     if root is None:
#         return []
#
#     return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def preorder_traversal(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    result: list[int | None] = []
    stack: list[TreeNode | None] = [root]

    while stack:
        node = stack.pop()
        if node is None:
            continue

        result.append(node.val)

        stack.append(node.right)
        stack.append(node.left)

    return result
