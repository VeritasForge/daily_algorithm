import pytest

from src.common.linked_list import ListNode, create_intersecting_lists
from src.leetcode.intersection_of_two_linked_lists_160 import get_intersection_node


@pytest.mark.parametrize(
    "list_a, list_b, skip_a, skip_b",
    [
        # LeetCode 기본 예제
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3),
        ([1, 9, 1, 2, 4], [3, 2, 4], 3, 1),
        ([2, 6, 4], [1, 5], 3, 2),
        # 보강 - 엣지 케이스
        ([2], [2], 0, 0),  # 단일 노드 리스트가 완전히 겹치는 경우
        ([1, 2, 3], [3], 2, 0),  # 짧은 리스트 전체가 교차 지점인 경우
        # 보강 - 예외 케이스
        ([1], [2], 1, 1),  # 각각 단일 노드이며 교차하지 않는 경우
    ],
)
def test_get_intersection_node(
    list_a: list[int], list_b: list[int], skip_a: int, skip_b: int
) -> None:
    head_a, head_b = create_intersecting_lists(list_a, list_b, skip_a, skip_b)

    expected: ListNode | None = head_a
    for _ in range(skip_a):
        assert expected is not None
        expected = expected.next

    assert get_intersection_node(head_a, head_b) is expected
