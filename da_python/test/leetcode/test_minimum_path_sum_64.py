import pytest

from src.leetcode.minimum_path_sum_64 import min_path_sum

pytestmark = pytest.mark.skip(reason="WIP")


@pytest.mark.parametrize(
    "grid, expected",
    [
        # LeetCode 기본 예제
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
        # 보강 - 엣지 케이스: 1x1 그리드
        ([[0]], 0),
        ([[5]], 5),
        # 보강 - 엣지 케이스: 단일 행
        ([[1, 2, 3, 4]], 10),
        # 보강 - 엣지 케이스: 단일 열
        ([[1], [2], [3]], 6),
        # 보강 - 모든 값이 0
        ([[0, 0], [0, 0]], 0),
        # 보강 - 아래로 가는 게 유리한 경우
        ([[1, 100], [1, 1]], 3),
        # 보강 - 오른쪽으로 가는 게 유리한 경우
        ([[1, 1], [100, 1]], 3),
        # 보강 - 최댓값 경계
        ([[200, 200], [200, 200]], 600),
    ],
)
def test_min_path_sum(grid: list[list[int]], expected: int) -> None:
    assert min_path_sum(grid) == expected
