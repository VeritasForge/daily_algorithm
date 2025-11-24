import pytest

from collections import deque

from src.leetcode.maximum_depth_of_binary_tree_104 import max_depth, TreeNode


# def list_to_tree(nodes: list[int]) -> TreeNode | None:
#     if not nodes:
#         return None
#
#     it = iter(nodes)
#     val = next(it)
#     if val is None:
#         return None
#
#     root = TreeNode(val)
#     q = [root]
#     for node in q:
#         try:
#             val = next(it)
#             if val is not None:
#                 node.left = TreeNode(val)
#                 q.append(node.left)
#             val = next(it)
#             if val is not None:
#                 node.right = TreeNode(val)
#                 q.append(node.right)
#         except StopIteration:
#             break
#     return root


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
#
#         try:
#             val = next(it)
#             if val is not None:
#                 node.left = TreeNode(val)
#                 q.append(node.left)
#
#             val = next(it)
#             if val is not None:
#                 node.right = TreeNode(val)
#                 q.append(node.right)
#         except StopIteration:
#             break
#
#     return root


def list_to_tree(nodes: list[int]) -> TreeNode | None:
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


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([0], 1),
    ],
)
def test_max_depth(nodes, expected):
    root = list_to_tree(nodes)
    assert max_depth(root) == expected
