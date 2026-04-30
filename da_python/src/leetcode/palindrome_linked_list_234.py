"""
https://leetcode.com/problems/palindrome-linked-list

234. Palindrome Linked List (Easy)

Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    - The number of nodes in the list is in the range [1, 10^5].
    - 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from src.common.linked_list import ListNode


def is_palindrome(head: ListNode | None) -> bool:
    if head is None or head.next is None:
        return True

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True
