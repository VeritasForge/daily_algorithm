import pytest

from src.leetcode.majority_element_ii_229 import majority_element

pytestmark = pytest.mark.skip(reason="WIP")


@pytest.mark.parametrize(
    "nums, expected",
    [
        # 기본 예제
        ([3, 2, 3], [3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        # 과반수 원소가 2개인 케이스
        ([1, 1, 1, 2, 2, 2, 3], [1, 2]),
        # 과반수 원소가 없는 케이스
        ([1, 2, 3], []),
        ([1, 2, 3, 4], []),
        # 모든 원소가 같은 케이스
        ([5, 5, 5], [5]),
        # 엣지 케이스 - 음수
        ([-1, -1, -1, 2, 3], [-1]),
        # 엣지 케이스 - 경계값
        ([0, 0, 0], [0]),
        # 정확히 n/3번 등장 (포함되지 않아야 함)
        ([1, 1, 2, 2, 3, 3], []),
        # n/3 + 1번 등장
        ([1, 1, 1, 2, 3, 4, 5], [1]),
    ],
)
def test_majority_element(nums: list[int], expected: list[int]):
    result = majority_element(nums)
    assert sorted(result) == sorted(expected)
