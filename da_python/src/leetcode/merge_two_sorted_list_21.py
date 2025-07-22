"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def node_to_list(node: ListNode | None) -> list[int]:
    as_list: list[int] = []
    if node is None:
        return as_list

    head = node
    while head:
        as_list.append(head.val)
        head = head.next_node

    return as_list


def merge_two_list(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if not list1 and not list2:
        return None

    arr = node_to_list(list1)
    arr += node_to_list(list2)

    if not arr:
        return None

    arr.sort()

    result = head = ListNode(val=arr[0])
    for v in arr[1:]:
        head.next_node = head = ListNode(val=v)

    return result
