import pytest

from src.common.linked_list import create_linked_list
from src.leetcode.palindrome_linked_list_234 import is_palindrome


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # LeetCode 기본 예제
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        # 보강 - 엣지 케이스 (제약 조건 최소 길이 1)
        ([1], True),
        # 보강 - 홀수 길이 회문
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
        # 보강 - 짝수 길이 비회문
        ([1, 2, 3, 4], False),
        # 보강 - 모두 같은 값
        ([7, 7, 7, 7], True),
        # 보강 - 두 노드 동일
        ([1, 1], True),
        # 보강 - Node.val 경계값 (0 포함)
        ([0, 9, 0], True),
        ([0, 0, 9], False),
    ],
)
def test_is_palindrome(input_list: list[int], expected: bool):
    head = create_linked_list(input_list)
    assert is_palindrome(head) == expected
