import pytest
from typing import Optional, List
from src.leetcode.remove_duplicates_from_sorted_list_83 import (
    deleteDuplicates,
    ListNode,
)


# Helper function to convert a list to a ListNode
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert a ListNode to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),  # Empty list
        ([1], [1]),  # Single element list
        ([1, 1, 1, 1], [1]),  # All duplicates
    ],
)
def test_delete_duplicates(input_list: List[int], expected_list: List[int]):
    head = list_to_linked_list(input_list)
    result_head = deleteDuplicates(head)
    assert linked_list_to_list(result_head) == expected_list
