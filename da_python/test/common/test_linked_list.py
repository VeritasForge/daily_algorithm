import pytest

from src.common.linked_list import create_linked_list, create_list


class TestCreateLinkedList:
    @pytest.mark.parametrize(
        "nums",
        [
            [0],
            [1, 1],
            [1, 2, 3],
        ],
    )
    def test_create_linked_list(self, nums: list[int]):
        head = create_linked_list(nums)
        for n in nums:
            assert head is not None
            assert head.val == n
            head = head.next_node

        assert head is None

    def test_create_linked_list_with_empty_list(self):
        head = create_linked_list([])

        assert head is None


class TestCreateList:
    @pytest.mark.parametrize(
        "nums",
        [
            [],
            [1],
            [1, 1],
            [1, 2, 3],
        ],
    )
    def test_create_list(self, nums):
        head = create_linked_list(nums)

        res = create_list(head)

        assert res == nums

    def test_create_list_with_none_param(self):
        assert create_list(None) == []
