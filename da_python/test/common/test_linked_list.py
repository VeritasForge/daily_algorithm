import pytest

from src.common.linked_list import (
    create_linked_list,
    create_linked_list_with_cycle,
    create_list,
)


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
            head = head.next

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


class TestCreateLinkedListWithCycle:
    def test_create_linked_list_with_cycle_case_1(self):
        head = create_linked_list_with_cycle([3, 2, 0, -4], 1)

        # Then:
        node_3 = head
        node_2 = head.next
        node_0 = head.next.next
        node_4 = head.next.next.next

        assert node_3.val == 3
        assert node_2.val == 2
        assert node_0.val == 0
        assert node_4.val == -4

        assert node_4.next is node_2

    def test_create_linked_list_with_cycle_case_2(self):
        head = create_linked_list_with_cycle([1, 2], 0)

        # Then:
        node_1 = head
        node_2 = head.next

        assert node_1.val == 1
        assert node_2.val == 2

        assert node_2.next is node_1

    def test_create_linked_list_with_cycle_case_3(self):
        head = create_linked_list_with_cycle([1], -1)

        # Then:
        assert head.val == 1
        assert head.next is None

    def test_create_linked_list_with_cycle_case_4(self):
        head = create_linked_list_with_cycle([], -1)

        # Then:
        assert head is None
