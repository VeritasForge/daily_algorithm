from src.common.linked_list import ListNode, create_list

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


def merge_two_list(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    return way_2(list1, list2)


def way_1(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if not list1 and not list2:
        return None

    arr = create_list(list1)
    arr += create_list(list2)

    if not arr:
        return None

    arr.sort()

    result = head = ListNode(val=arr[0])
    for v in arr[1:]:
        head.next = head = ListNode(val=v)

    return result


def way_2(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    result = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
    head.next = list1 or list2
    return result.next
