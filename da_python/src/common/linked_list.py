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
