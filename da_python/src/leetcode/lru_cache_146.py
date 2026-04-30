"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Difficulty: Medium

문제 설명:
    Least Recently Used (LRU) 캐시의 제약 조건을 따르는 자료구조를 설계하라.

    LRUCache 클래스를 구현한다:
    - LRUCache(int capacity): 양의 정수 capacity로 LRU 캐시를 초기화한다.
    - int get(int key): key가 존재하면 value를 반환하고, 그렇지 않으면 -1을 반환한다.
    - void put(int key, int value): key가 존재하면 value를 갱신하고,
      존재하지 않으면 key-value 쌍을 캐시에 추가한다.
      이 연산으로 인해 키 개수가 capacity를 초과하면 가장 오래 사용되지 않은 key를 제거한다.

    get과 put 함수는 평균 O(1) 시간 복잡도로 동작해야 한다.

제약 조건:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - get과 put은 최대 2 * 10^5번 호출된다.
"""

from __future__ import annotations


# @dataclass
# class Node:
#     key: int
#     value: int
#     prev: Node | None = None
#     next: Node | None = None
#
#
# class LRUCache:
#     def __init__(self, capacity: int) -> None:
#         self.cache: dict[int, Node] = {}
#         self.capacity: int = capacity
#
#         self.head: Node = Node(0, 0)
#         self.tail: Node = Node(0, 0)
#
#         self.head.next, self.tail.prev = self.tail, self.head
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#
#         node = self.cache[key]
#         self._move_to_mru(node)
#
#         return node.value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#
#             self._move_to_mru(node)
#             return
#
#         if len(self.cache) >= self.capacity:
#             assert self.head.next is not None
#
#             del self.cache[self.head.next.key]
#
#             self.head.next = self.head.next.next
#             self.head.next.next.prev = self.head
#
#         node = Node(key, value, self.tail.prev, self.tail)
#         self.cache[key] = node
#
#         assert self.tail.prev is not None
#         self.tail.prev.next = node
#         self.tail.prev = node
#
#     def _move_to_mru(self, node: Node) -> None:
#         assert node.prev is not None and node.next is not None
#         node.prev.next, node.next.prev = node.next, node.prev
#
#         node.prev, node.next = self.tail.prev, self.tail
#
#         assert self.tail.prev is not None
#         self.tail.prev.next = node
#         self.tail.prev = node
#

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


# class LRUCache:
#     def __init__(self, capacity: int) -> None:
#         self.cache = {}
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#
#         value = self.cache.pop(key)
#         self.cache[key] = value
#
#         return value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             del self.cache[key]
#         elif len(self.cache) >= self.capacity:
#             del self.cache[next(iter(self.cache))]
#
#         self.cache[key] = value
