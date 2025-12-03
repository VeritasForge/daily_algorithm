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
