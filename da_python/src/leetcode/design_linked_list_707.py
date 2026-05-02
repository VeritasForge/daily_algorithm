"""
707. Design Linked List
https://leetcode.com/problems/design-linked-list/

Difficulty: Medium

문제 설명:
    Linked list 자료구조를 직접 구현한다. Singly 또는 doubly linked list 중 선택할 수 있다.
    Singly linked list의 노드는 두 가지 속성을 가진다: val(값)과 next(다음 노드 포인터).
    Doubly linked list라면 prev(이전 노드 포인터) 속성이 추가된다.
    모든 노드는 0-indexed로 가정한다.

    MyLinkedList 클래스를 구현하라:
        - MyLinkedList(): MyLinkedList 객체를 초기화한다.
        - int get(int index): index 번째 노드의 값을 반환한다. 유효하지 않은 인덱스면 -1을 반환한다.
        - void add_at_head(int val): val 값을 가진 노드를 리스트 맨 앞에 추가한다.
        - void add_at_tail(int val): val 값을 가진 노드를 리스트 맨 뒤에 추가한다.
        - void add_at_index(int index, int val): index 번째 노드 앞에 val 값을 가진 노드를 추가한다.
            index == length이면 맨 뒤에 추가한다.
            index > length이면 추가하지 않는다.
        - void delete_at_index(int index): index 번째 노드를 삭제한다 (유효한 인덱스인 경우).

제약 조건:
    - 0 <= index, val <= 1000
    - 내장 LinkedList 라이브러리 사용 금지
    - get, add_at_head, add_at_tail, add_at_index, delete_at_index 호출은 최대 2000회
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    prev: Node | None = None
    next: Node | None = None


class MyLinkedList:
    def __init__(self) -> None:
        self.head: Node = Node(0)
        self.tail: Node = Node(0)
        self.count = 0

    def get(self, index: int) -> int:
        found = self._find(index)
        if found is None:
            return -1

        return found.val

    def add_at_head(self, val: int) -> None:
        if self.count == 0:
            assert self.head.next is None and self.tail.prev is None
            self.head.next = self.tail.prev = Node(val, self.head, self.tail)
        else:
            node = Node(val, prev=self.head, next=self.head.next)
            assert self.head.next
            self.head.next.prev = node
            self.head.next = node

        self.count += 1

    def add_at_tail(self, val: int) -> None:
        if self.count == 0:
            assert self.head.next is None and self.tail.prev is None
            self.head.next = self.tail.prev = Node(val, self.head, self.tail)
        else:
            node = Node(val, self.tail.prev, self.tail)
            assert self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node

        self.count += 1

    def add_at_index(self, index: int, val: int) -> None:
        if self.count == 0:
            self.add_at_head(val)
            return

        if self.count == index:
            self.add_at_tail(val)
            return

        found = self._find(index)
        if found is None:
            return

        node = Node(val, found.prev, found)
        assert found.prev is not None
        found.prev.next = node
        found.prev = node

        self.count += 1

    def delete_at_index(self, index: int) -> None:
        found = self._find(index)
        if found is None:
            return

        assert found.prev is not None and found.next is not None
        found.prev.next = found.next
        found.next.prev = found.prev

        self.count -= 1

    def _find(self, index: int) -> Node | None:
        # if self.head.next is None or self.count - 1 < index or index < 0:
        if self.count - 1 < index or index < 0:
            return None

        curr = self.head.next
        while index > 0 and curr is not None:
            curr = curr.next
            index -= 1

        return curr
