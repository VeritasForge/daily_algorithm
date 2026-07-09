import pytest

from src.leetcode.contains_duplicate_ii_219 import contains_nearby_duplicate


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # LeetCode 기본 예제
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        # 보강 - 엣지 케이스 (단일 원소, k=0)
        ([1], 0, False),
        ([1, 1], 0, False),
        # 보강 - 예외 케이스 (경계 거리 정확히 일치/초과)
        ([1, 2, 1], 2, True),
        ([1, 2, 3, 1], 2, False),
        # 보강 - 예외 케이스 (음수 값)
        ([-1, -1], 1, True),
        # 보강 - 추가 검증 (연속 중복, k가 배열 길이보다 큰 경우)
        ([1, 1, 1, 1], 1, True),
        ([1, 2, 3, 4], 100, False),
    ],
)
def test_contains_nearby_duplicate(nums: list[int], k: int, expected: bool):
    assert contains_nearby_duplicate(nums, k) == expected
