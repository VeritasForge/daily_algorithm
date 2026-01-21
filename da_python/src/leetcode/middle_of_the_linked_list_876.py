# https://leetcode.com/problems/middle-of-the-linked-list
# 876. Middle of the Linked List
# Difficulty: Easy
#
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4,
# we return the second one.

from src.common.linked_list import ListNode


# def middle_node(head: ListNode | None) -> ListNode | None:
#     if head is None:
#         return None
#
#     count = 1
#     curr = head
#     while curr.next is not None:
#         curr = curr.next
#         count += 1
#
#     m_node = head
#     for _ in range(count // 2):
#         m_node = m_node.next
#
#     return m_node


def middle_node(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow