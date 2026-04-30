from src.leetcode.lru_cache_146 import LRUCache


# LeetCode 기본 예제
def test_lru_cache_example_1() -> None:
    cache = LRUCache(1)

    cache.put(1, 1)
    assert cache.get(1) == 1


def test_lru_cache_example_2() -> None:
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    assert cache.get(2) == 2


def test_lru_cache_example_3() -> None:
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)

    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3


def test_lru_cache_example_4() -> None:
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1

    cache.put(3, 3)

    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_lru_cache_example1() -> None:
    """
    Input:
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
    """
    cache = LRUCache(2)

    cache.put(1, 1)  # cache is {1=1}
    cache.put(2, 2)  # cache is {1=1, 2=2}
    assert cache.get(1) == 1  # return 1
    cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert cache.get(2) == -1  # not found

    cache.put(4, 4)
    assert cache.get(1) == -1  # not found
    assert cache.get(3) == 3
    assert cache.get(4) == 4


# 보강 - 엣지 케이스: capacity가 1인 경우
def test_lru_cache_capacity_one() -> None:
    cache = LRUCache(1)
    cache.put(1, 100)
    assert cache.get(1) == 100
    cache.put(2, 200)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 200


# 보강 - 엣지 케이스: 존재하지 않는 key 조회
def test_lru_cache_get_missing_key() -> None:
    cache = LRUCache(2)
    assert cache.get(0) == -1
    cache.put(1, 1)
    assert cache.get(99) == -1


# 보강 - 예외 케이스: 기존 key 갱신은 eviction을 일으키지 않는다
def test_lru_cache_put_existing_key_no_eviction() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(2, 20)  # 갱신만 — eviction이 일어나면 안 됨
    assert cache.get(1) == 1  # key 1 보존 확인
    assert cache.get(2) == 20  # key 2 새 값 확인


# 보강 - 예외 케이스: 같은 key를 update하면 LRU 순서가 갱신된다
def test_lru_cache_update_existing_key_refreshes_order() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # update key 1, key 2 becomes LRU
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 3


# 보강 - 예외 케이스: get 호출도 LRU 순서를 갱신한다
def test_lru_cache_get_refreshes_order() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # key 2 becomes LRU
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3


# 보강 - 추가 검증: value가 0인 경우 (-1 반환과 구분)
def test_lru_cache_zero_value() -> None:
    cache = LRUCache(2)
    cache.put(1, 0)
    assert cache.get(1) == 0
    assert cache.get(2) == -1


# 보강 - 추가 검증: 연속 put/get 혼합 시나리오
def test_lru_cache_mixed_operations() -> None:
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == 1  # order: 2, 3, 1
    cache.put(4, 4)  # evicts key 2, order: 3, 1, 4
    assert cache.get(2) == -1
    assert cache.get(3) == 3  # order: 1, 4, 3
    cache.put(5, 5)  # evicts key 1, order: 4, 3, 5
    assert cache.get(1) == -1
    assert cache.get(4) == 4
    assert cache.get(5) == 5
