# LeetCode 자료구조 구현 문제 추천

> 📅 작성일: 2026-04-30
> 🎯 목적: 주요 자료구조 구현 문제를 카테고리별/난이도별로 정리하여 학습 로드맵 제공

---

## 🎯 학습 로드맵 (난이도 흐름)

```
선형 자료구조 → 트리 → 해시 → 힙 → 트라이 → 고급(LFU/Skip List/Segment Tree)
```

> 💡 `Doubly Linked List + Hash Map 조합` 구간(146 LRU Cache)을 통과하면 자연스럽게 460 LFU, 환형 큐로 흐름이 이어집니다.

---

## 📋 카테고리별 추천 문제

### 1️⃣ Linked List (단일 연결 리스트)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| **707** | Design Linked List | 🟡 Medium | ⭐ 직접 구현 (필수) |
| 206 | Reverse Linked List | 🟢 Easy | 포인터 조작 기본 |
| 21 | Merge Two Sorted Lists | 🟢 Easy | 더미 노드 패턴 |
| 141 | Linked List Cycle | 🟢 Easy | Floyd 알고리즘 |
| 92 | Reverse Linked List II | 🟡 Medium | 부분 reverse |
| 25 | Reverse Nodes in k-Group | 🔴 Hard | 그룹 단위 reverse |

### 2️⃣ Doubly Linked List (이중 연결 리스트)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| **146** | LRU Cache | 🟡 Medium | ⭐⭐ DLL + HashMap |
| 460 | LFU Cache | 🔴 Hard | DLL + HashMap 2개 |
| 432 | All O'one Data Structure | 🔴 Hard | Bucket 기반 DLL |
| 1472 | Design Browser History | 🟡 Medium | 양방향 탐색 |

### 3️⃣ Stack

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 20 | Valid Parentheses | 🟢 Easy | Stack 입문 |
| **155** | Min Stack | 🟢 Easy | ⭐ O(1) min 추적 |
| 232 | Queue using Stacks | 🟢 Easy | 두 스택으로 큐 |
| 225 | Stack using Queues | 🟢 Easy | 큐로 스택 |
| 150 | Evaluate Reverse Polish | 🟡 Medium | 후위 표기법 |
| 394 | Decode String | 🟡 Medium | 중첩 처리 |
| 739 | Daily Temperatures | 🟡 Medium | **Monotonic Stack** |
| 84 | Largest Rectangle in Histogram | 🔴 Hard | Monotonic Stack 끝판 |
| 42 | Trapping Rain Water | 🔴 Hard | 다양한 풀이 |

### 4️⃣ Queue & Circular Queue (환형 큐)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 933 | Number of Recent Calls | 🟢 Easy | 큐 활용 |
| **622** | Design Circular Queue | 🟡 Medium | ⭐ 환형 큐 직접 구현 |
| **641** | Design Circular Deque | 🟡 Medium | ⭐ 환형 덱 |
| 353 | Design Snake Game | 🟡 Medium | 큐 응용 |
| 239 | Sliding Window Maximum | 🔴 Hard | **Monotonic Deque** |

### 5️⃣ Deque (덱)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 641 | Design Circular Deque | 🟡 Medium | 위와 동일 |
| **1670** | Design Front Middle Back Queue | 🟡 Medium | ⭐ 두 덱으로 중간 접근 |
| 239 | Sliding Window Maximum | 🔴 Hard | 단조 덱 |

### 6️⃣ Hash Map / Hash Set

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| **705** | Design HashSet | 🟢 Easy | ⭐ 충돌 처리 학습 |
| **706** | Design HashMap | 🟢 Easy | ⭐ Chaining/Open Addressing |
| 380 | Insert Delete GetRandom O(1) | 🟡 Medium | HashMap + Array |
| 381 | ↑ Duplicates allowed | 🔴 Hard | 위 변형 |

### 7️⃣ Heap / Priority Queue

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 703 | Kth Largest in a Stream | 🟢 Easy | Min-heap 기본 |
| 1046 | Last Stone Weight | 🟢 Easy | Max-heap |
| 215 | Kth Largest Element | 🟡 Medium | Heap vs QuickSelect |
| 973 | K Closest Points to Origin | 🟡 Medium | 거리 기반 heap |
| **295** | Find Median from Data Stream | 🔴 Hard | ⭐⭐ Two heaps |
| 23 | Merge k Sorted Lists | 🔴 Hard | Heap + LinkedList |

### 8️⃣ Trie (트라이)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| **208** | Implement Trie (Prefix Tree) | 🟡 Medium | ⭐ 입문 필수 |
| **211** | Add and Search Word | 🟡 Medium | ⭐ Trie + DFS (와일드카드) |
| 648 | Replace Words | 🟡 Medium | Trie 검색 응용 |
| 1268 | Search Suggestions System | 🟡 Medium | Trie + 자동완성 |
| 212 | Word Search II | 🔴 Hard | Trie + Backtracking |
| 642 | Design Search Autocomplete | 🔴 Hard | Trie + 빈도 |
| 1032 | Stream of Characters | 🔴 Hard | Reverse Trie |

### 9️⃣ Tree / BST

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 700 | Search in BST | 🟢 Easy | BST 기본 |
| 701 | Insert into BST | 🟡 Medium | BST 삽입 |
| **173** | BST Iterator | 🟡 Medium | ⭐ Stack으로 in-order |
| 449 | Serialize/Deserialize BST | 🟡 Medium | 직렬화 |
| 297 | Serialize/Deserialize Binary Tree | 🔴 Hard | 일반 트리 직렬화 |

### 🔟 Union Find (Disjoint Set)

| 번호 | 제목 | 난이도 | 포인트 |
|------|------|--------|--------|
| 547 | Number of Provinces | 🟡 Medium | UF 입문 |
| 684 | Redundant Connection | 🟡 Medium | 사이클 탐지 |
| **721** | Accounts Merge | 🟡 Medium | ⭐ UF 응용 |
| 685 | Redundant Connection II | 🔴 Hard | 방향 그래프 UF |

### 1️⃣1️⃣ 고급 (Advanced)

| 번호 | 제목 | 난이도 | 자료구조 |
|------|------|--------|---------|
| 307 | Range Sum Query - Mutable | 🟡 Medium | **Segment Tree / BIT** |
| 308 | Range Sum Query 2D - Mutable | 🔴 Hard | 2D BIT |
| 315 | Count Smaller Numbers After Self | 🔴 Hard | BIT/Merge Sort |
| **1206** | Design Skiplist | 🔴 Hard | ⭐ Skip List |
| 588 | Design In-Memory File System | 🔴 Hard | Trie 응용 |

---

## 🗺️ 추천 학습 순서

```
146 LRU Cache  (현재)
   ↓
460 LFU Cache         ← DLL + 두 HashMap
   ↓
622 Circular Queue    ← 환형 자료구조 입문
   ↓
641 Circular Deque
   ↓
208 Trie              ← 트리 계열 전환
   ↓
211 Add Search Word
   ↓
295 Find Median       ← Two Heaps 패턴
   ↓
239 Sliding Window Max ← Monotonic Deque
```

---

## 💡 비유로 이해하기

| 자료구조 | 현실 비유 |
|---------|----------|
| Linked List | 🚂 기차 (각 칸이 다음 칸 연결고리만 가짐) |
| Doubly Linked List | 🚂 양방향 기차 (앞뒤 연결) |
| Stack | 🥞 팬케이크 더미 (위에서만 쌓고 빼기) |
| Queue | 🚶‍♂️🚶‍♀️ 줄서기 (앞에서 빼고 뒤에서 추가) |
| Circular Queue | 🎡 회전목마 (끝나면 다시 처음으로) |
| Deque | 🎫 양방향 출입구 매표소 |
| Trie | 📚 사전 (공통 접두어 공유) |
| Heap | 🏆 토너먼트 (1등이 항상 꼭대기) |
| Union Find | 👥 친구 그룹 묶기 |
| LRU Cache | 🎮 최근 플레이 게임 목록 |

---

## ⚠️ 추가 학습 포인트

1. **Monotonic Stack/Queue 패턴**은 별도 챕터로 깊이 파야 합니다 (84, 239, 739가 입문)
2. **LeetCode Explore 카드** 활용 가능: `Trie`, `Queue & Stack`, `Linked List` 카드가 잘 정리되어 있음
3. **CPython 표준 라이브러리 비교 학습**: 직접 구현 후 `collections.deque`, `heapq`, `OrderedDict` 소스를 읽어보면 좋음

---

## 🏷️ 범례

- 🟢 Easy / 🟡 Medium / 🔴 Hard
- ⭐ 추천 / ⭐⭐ 강력 추천 (자료구조 대표 문제)
