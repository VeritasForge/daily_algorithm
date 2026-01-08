"""
https://leetcode.com/problems/reverse-linked-list

206. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

from src.common.linked_list import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head

    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


# def reverse_list(head: ListNode | None) -> ListNode | None:
#     prev, curr = None, head
#     while curr:
#         curr.next, prev, curr = prev, curr, curr.next
#     return prev
