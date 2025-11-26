from __future__ import annotations
import pytest

from src.common.tree import TreeNode, find_node, list_to_tree


# Helper function to build a tree from a list (LeetCode style)
def build_tree(nodes: list[int | None]) -> TreeNode | None:
    if not nodes:
        return None
    nodes_copy = nodes[:]  # Create a copy
    val = nodes_copy.pop(0)
    if val is None:
        return None
    root = TreeNode(val)
    queue = [root]
    while nodes_copy:
        current = queue.pop(0)
        left_val = nodes_copy.pop(0)
        if left_val is not None:
            current.left = TreeNode(left_val)
            queue.append(current.left)
        if nodes_copy:
            right_val = nodes_copy.pop(0)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
    return root


class TestListToTree:
    def test_list_to_tree_1(self):
        root = list_to_tree([])

        assert root is None

    def test_list_to_tree_2(self):
        root = list_to_tree([0])

        assert root.val == 0
        assert root.left is None
        assert root.right is None

    def test_list_to_tree_3(self):
        root = list_to_tree([1, None, 2])

        assert root.val == 1

        left = root.left
        right = root.right

        assert left is None
        assert right.val == 2

        right_left = right.left
        right_right = right.right

        assert right_left is None
        assert right_right is None

    def test_list_to_tree_4(self):
        root = list_to_tree([3, 9, 20, None, None, 15, 7])

        assert root.val == 3

        left = root.left
        right = root.right
        assert left.val == 9
        assert right.val == 20

        left_left = left.left
        left_right = left.right
        assert left_left is None
        assert left_right is None

        right_left = right.left
        right_right = right.right
        assert right_left.val == 15
        assert right_right.val == 7

        right_left_left = right_left.left
        right_left_right = right_left.right
        assert right_left_left is None
        assert right_left_right is None

        right_right_left = right_right.left
        right_right_right = right_right.right
        assert right_right_left is None
        assert right_right_right is None


class TestFindNode:
    @pytest.mark.parametrize("val", [6, 2, 8, 0, 4, 7, 9, 3, 5])
    def test_find_node(self, val: int):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

        found_node = find_node(root, val)

        assert found_node is not None
        assert found_node.val == val

    @pytest.mark.parametrize("val", [1, 10])
    def test_should_return_none_there_is_no_node(self, val: int):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

        found_node = find_node(root, val)

        assert found_node is None
