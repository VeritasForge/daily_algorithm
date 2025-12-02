from __future__ import annotations
import pytest

from src.common.tree import find_node, list_to_tree, tree_to_list


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


class TestTreeToList:
    @pytest.mark.parametrize(
        "nodes",
        [
            [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            [4, 2, 7, 1, 3, 6, 9],
            [2, 1, 3],
            [1, 2, 3, None, None, 4],
        ],
    )
    def test_tree_to_list(self, nodes):
        root = list_to_tree(nodes)

        result = tree_to_list(root)

        assert result == nodes


class TestFindNode:
    @pytest.mark.parametrize("val", [6, 2, 8, 0, 4, 7, 9, 3, 5])
    def test_find_node(self, val: int):
        root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

        found_node = find_node(root, val)

        assert found_node is not None
        assert found_node.val == val

    @pytest.mark.parametrize("val", [1, 10])
    def test_should_return_none_there_is_no_node(self, val: int):
        root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

        found_node = find_node(root, val)

        assert found_node is None
