"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Difficulty: Easy

문제 설명:
    Given the head of a linked list and an integer val, remove all the nodes
    of the linked list that has Node.val == val, and return the new head.

    Example 1:

    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

    Example 2:

    Input: head = [], val = 1
    Output: []

    Example 3:

    Input: head = [7,7,7,7], val = 7
    Output: []

제약 조건:
    The number of nodes in the list is in the range [0, 10^4].
    1 <= Node.val <= 50
    0 <= val <= 50
"""

from src.common.linked_list import ListNode


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    dummy = ListNode(0, head)
    prev, curr = dummy, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy.next


# def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
#     prev, curr = None, head
#     while curr:
#         if curr.val == val:
#             if prev is None:
#                 head = curr = curr.next
#             else:
#                 prev.next = curr = curr.next
#         else:
#             prev, curr = curr, curr.next
#     return head
