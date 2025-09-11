# Problem: 83. Remove Duplicates from Sorted List
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
#
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode | None) -> Optional[ListNode]:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
