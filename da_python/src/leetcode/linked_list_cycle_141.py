# https://leetcode.com/problems/linked-list-cycle/
# 141. Linked List Cycle (Easy)
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
#   Input: head = [3,2,0,-4], pos = 1
#   Output: true
#   Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
#   Input: head = [1,2], pos = 0
#   Output: true
#   Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
#   Input: head = [1], pos = -1
#   Output: false
#   Explanation: There is no cycle in the linked list.
#
# Constraints:
#   - The number of nodes in the list is in the range [0, 10^4].
#   - -10^5 <= Node.val <= 10^5
#   - pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from src.common.linked_list import ListNode


def has_cycle(head: ListNode | None) -> bool:
    return has_cyle_with_set(head)


def has_cycle_with_two_pointer(head: ListNode | None) -> bool:
    slow = fast = head

    while fast and fast.next:
        assert slow
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def has_cyle_with_set(head: ListNode | None) -> bool:
    if head is None:
        return False

    visit = set()
    curr: ListNode | None = head
    while curr:
        if id(curr) in visit:
            return True

        visit.add(id(curr))
        curr = curr.next

    return False
