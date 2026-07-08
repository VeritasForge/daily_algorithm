import pytest

from src.common.linked_list import create_linked_list, create_list
from src.leetcode.remove_linked_list_elements_203 import remove_elements


@pytest.mark.parametrize(
    "head, val, expected",
    [
        # LeetCode 기본 예제
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, []),
        # 보강 - 엣지 케이스 (빈 리스트, 단일 노드)
        ([1], 1, []),
        ([1], 2, [1]),
        # 보강 - 예외 케이스 (헤드/테일에서 제거, 연속된 중복)
        ([6, 1, 2, 3], 6, [1, 2, 3]),
        ([1, 2, 3, 6], 6, [1, 2, 3]),
        ([1, 6, 6, 2], 6, [1, 2]),
        # 보강 - 추가 검증 (제약 조건 경계값 val=1, val=50, val=0)
        ([1, 1, 1], 1, []),
        ([50, 1, 50], 50, [1]),
        ([1, 2, 3], 0, [1, 2, 3]),
    ],
)
def test_remove_elements(head: list[int], val: int, expected: list[int]):
    result = remove_elements(create_linked_list(head), val)
    assert create_list(result) == expected
