"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Difficulty: Easy

문제 설명:
    두 단일 연결 리스트 headA, headB가 주어질 때, 두 리스트가 교차하는 지점의
    노드를 반환합니다. 교차하지 않으면 None을 반환합니다.
    교차 여부는 노드의 값이 아니라 노드 자체(참조)가 같은지로 판단합니다.
    함수가 반환된 후에도 두 리스트는 원래 구조를 유지해야 합니다.

제약 조건:
    - listA의 노드 개수는 m, listB의 노드 개수는 n입니다.
    - 1 <= m, n <= 3 * 10^4
    - 1 <= Node.val <= 10^5
    - 0 <= skipA <= m
    - 0 <= skipB <= n
    - 두 리스트가 교차하지 않으면 intersectVal은 0입니다.
    - 두 리스트가 교차하면 intersectVal == listA[skipA] == listB[skipB]입니다.

Follow up: O(m + n) 시간, O(1) 공간으로 풀 수 있나요?
"""

from src.common.linked_list import ListNode


def get_intersection_node(
    head_a: ListNode | None, head_b: ListNode | None
) -> ListNode | None:
    if head_a is None or head_b is None:
        return None

    a, b = head_a, head_b

    while a is not b:
        a = head_b if a is None else a.next
        b = head_a if b is None else b.next

    return a
