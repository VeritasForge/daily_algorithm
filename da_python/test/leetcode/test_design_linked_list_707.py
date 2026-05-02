import pytest

from src.leetcode.design_linked_list_707 import MyLinkedList


def test_my_linked_list_example1() -> None:
    """
    LeetCode 기본 예제

    Input:  ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
            [[],             [1],         [3],         [1, 2],       [1],   [1],             [1]]
    Output: [null, null, null, null, 2, null, 3]
    """
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(3)
    obj.add_at_index(1, 2)  # 1 -> 2 -> 3
    assert obj.get(1) == 2
    obj.delete_at_index(1)  # 1 -> 3
    assert obj.get(1) == 3


# ---------------------------------------------------------------------------
# 보강 - 엣지 케이스: 빈 리스트
# ---------------------------------------------------------------------------
def test_get_on_empty_list_returns_minus_one() -> None:
    obj = MyLinkedList()
    assert obj.get(0) == -1
    assert obj.get(5) == -1


def test_delete_at_index_on_empty_list_is_noop() -> None:
    obj = MyLinkedList()
    obj.delete_at_index(0)  # 예외 없이 통과해야 함
    assert obj.get(0) == -1


# ---------------------------------------------------------------------------
# 보강 - 엣지 케이스: 단일 원소
# ---------------------------------------------------------------------------
def test_single_element_add_and_get() -> None:
    obj = MyLinkedList()
    obj.add_at_head(7)
    assert obj.get(0) == 7
    assert obj.get(1) == -1  # 범위 초과


def test_single_element_delete_makes_empty() -> None:
    obj = MyLinkedList()
    obj.add_at_head(7)
    obj.delete_at_index(0)
    assert obj.get(0) == -1


# ---------------------------------------------------------------------------
# 보강 - 예외 케이스: 음수 인덱스 / 범위 초과 인덱스
# ---------------------------------------------------------------------------
def test_get_with_negative_index_returns_minus_one() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)
    assert obj.get(-1) == -1


def test_get_out_of_bounds_returns_minus_one() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)
    assert obj.get(2) == -1
    assert obj.get(100) == -1


def test_add_at_index_greater_than_length_is_noop() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)  # 1 -> 2 (length=2)
    obj.add_at_index(5, 99)  # 5 > 2 이므로 추가되지 않음
    assert obj.get(0) == 1
    assert obj.get(1) == 2
    assert obj.get(2) == -1


def test_add_at_index_equals_length_appends_tail() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)  # 1 -> 2 (length=2)
    obj.add_at_index(2, 3)  # index == length 이므로 tail 에 추가
    assert obj.get(0) == 1
    assert obj.get(1) == 2
    assert obj.get(2) == 3


def test_add_at_index_zero_acts_like_head() -> None:
    obj = MyLinkedList()
    obj.add_at_tail(2)
    obj.add_at_tail(3)  # 2 -> 3
    obj.add_at_index(0, 1)  # 1 -> 2 -> 3
    assert obj.get(0) == 1
    assert obj.get(1) == 2
    assert obj.get(2) == 3


def test_delete_at_index_out_of_bounds_is_noop() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)
    obj.delete_at_index(5)  # 무시되어야 함
    obj.delete_at_index(-1)
    assert obj.get(0) == 1
    assert obj.get(1) == 2


# ---------------------------------------------------------------------------
# 보강 - 추가 검증: head/tail 전이 확인
# ---------------------------------------------------------------------------
def test_delete_head_updates_first_node() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)
    obj.add_at_tail(3)  # 1 -> 2 -> 3
    obj.delete_at_index(0)  # 2 -> 3
    assert obj.get(0) == 2
    assert obj.get(1) == 3
    assert obj.get(2) == -1


def test_delete_tail_updates_last_node() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_tail(2)
    obj.add_at_tail(3)  # 1 -> 2 -> 3
    obj.delete_at_index(2)  # 1 -> 2
    assert obj.get(0) == 1
    assert obj.get(1) == 2
    assert obj.get(2) == -1


def test_add_at_head_reverses_order() -> None:
    obj = MyLinkedList()
    obj.add_at_head(1)
    obj.add_at_head(2)
    obj.add_at_head(3)  # 3 -> 2 -> 1
    assert obj.get(0) == 3
    assert obj.get(1) == 2
    assert obj.get(2) == 1


# ---------------------------------------------------------------------------
# 보강 - 복합 시나리오: 다양한 연산 혼합
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "operations, expected",
    [
        # (operation, args) 시퀀스와 (op_index, expected_value) 검증 페어
        # - 다양한 연산 혼합 후 최종 상태 확인
        (
            [
                ("add_at_head", 7),
                ("add_at_head", 2),
                ("add_at_head", 1),
                ("add_at_index", 3, 0),  # 1 -> 2 -> 7 -> 0
                ("delete_at_index", 2),  # 1 -> 2 -> 0
                ("add_at_tail", 6),  # 1 -> 2 -> 0 -> 6
                ("add_at_head", 4),  # 4 -> 1 -> 2 -> 0 -> 6
            ],
            [4, 1, 2, 0, 6],
        ),
    ],
)
def test_mixed_operations(operations: list[tuple], expected: list[int]) -> None:
    obj = MyLinkedList()
    for op in operations:
        method = getattr(obj, op[0])
        method(*op[1:])

    for i, val in enumerate(expected):
        assert obj.get(i) == val
    # 끝 너머는 -1
    assert obj.get(len(expected)) == -1
