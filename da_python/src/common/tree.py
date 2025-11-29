from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int | None
    left: TreeNode | None = None
    right: TreeNode | None = None


# def list_to_tree(nodes: list[int]) -> TreeNode | None:
#     if not nodes:
#         return None
#
#     it = iter(nodes)
#     root = TreeNode(next(it))
#     q = deque([root])
#
#     while q:
#         node = q.popleft()
#         try:
#             val = next(it)
#             if val:
#                 node.left = TreeNode(val)
#                 q.append(node.left)
#
#             val = next(it)
#             if val:
#                 node.right = TreeNode(val)
#                 q.append(node.right)
#         except StopIteration:
#             break
#
#     return root


def list_to_tree(nodes: list[int | None]) -> TreeNode | None:
    if not nodes:
        return None

    root = head = TreeNode(nodes[0])
    q: deque[TreeNode] = deque()
    for idx, val in enumerate(nodes[1:]):
        if idx % 2 == 0 and val is not None:
            head.left = TreeNode(val)
            q.append(head.left)
        elif idx % 2 == 1 and val is not None:
            head.right = TreeNode(val)
            q.append(head.right)

        if idx % 2 == 1:
            head = q.popleft()

    return root


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None

    q = deque([root])

    while q:
        node = q.popleft()
        if node.val == val:
            return node

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return None
