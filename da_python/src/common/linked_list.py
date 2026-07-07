from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


def create_linked_list(nums: list[int]) -> ListNode | None:
    if not nums:
        return None

    head = curr = ListNode(nums[0])
    for i in range(1, len(nums)):
        curr.next = curr = ListNode(nums[i])
    return head


def create_list(node: ListNode | None) -> list[int]:
    arr: list[int] = []
    if node is None:
        return arr

    while node:
        arr.append(node.val)
        node = node.next

    return arr


def create_linked_list_with_cycle(values: list[int], pos: int) -> ListNode | None:
    """Create a linked list with a cycle at the given position.

    Args:
        values: List of node values.
        pos: Index of the node where the tail connects to (-1 for no cycle).

    Returns:
        Head of the linked list.
    """
    if not values:
        return None

    head = create_linked_list(values)
    assert head is not None
    if pos < 0:
        return head

    tail = head
    while tail and tail.next:
        tail = tail.next

    start_cycle: ListNode | None = head
    for _ in range(pos):
        assert start_cycle is not None
        start_cycle = start_cycle.next
    tail.next = start_cycle

    return head


def create_intersecting_lists(
    list_a: list[int], list_b: list[int], skip_a: int, skip_b: int
) -> tuple[ListNode | None, ListNode | None]:
    """Create two linked lists sharing a common tail starting at the given skip indices.

    Args:
        list_a: Full values of list A (including the shared tail).
        list_b: Full values of list B (including the shared tail).
        skip_a: Number of list A's own nodes before the shared tail (len(list_a) if none).
        skip_b: Number of list B's own nodes before the shared tail (len(list_b) if none).

    Returns:
        Tuple of (head_a, head_b).
    """
    tail = create_linked_list(list_a[skip_a:])

    def prepend(values: list[int], tail_node: ListNode | None) -> ListNode | None:
        if not values:
            return tail_node

        head = curr = ListNode(values[0])
        for val in values[1:]:
            curr.next = curr = ListNode(val)
        curr.next = tail_node
        return head

    return prepend(list_a[:skip_a], tail), prepend(list_b[:skip_b], tail)
