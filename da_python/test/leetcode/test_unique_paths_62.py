import pytest

from src.leetcode.unique_paths_62 import unique_paths


@pytest.mark.parametrize(
    "m, n, expected",
    [
        # LeetCode 기본 예제
        (3, 7, 28),
        (3, 2, 3),
        # 보강 - 엣지 케이스 (최솟값)
        (1, 1, 1),  # 1x1 격자: 시작점 == 도착점
        (1, 2, 1),  # 1행: 오른쪽으로만 이동
        (2, 1, 1),  # 1열: 아래로만 이동
        # 보강 - 엣지 케이스 (최댓값)
        (100, 1, 1),  # 큰 1열
        (1, 100, 1),  # 큰 1행
        # 보강 - 대칭성 검증 (m, n 교환 시 결과 동일)
        (2, 3, 3),
        (7, 3, 28),  # (3, 7)과 동일해야 함
        # 보강 - 추가 검증 (조합론 C(m+n-2, m-1))
        (3, 3, 6),  # C(4, 2) = 6
        (4, 4, 20),  # C(6, 3) = 20
        (5, 5, 70),  # C(8, 4) = 70
        # 보강 - 큰 입력
        (10, 10, 48620),  # C(18, 9) = 48620
    ],
)
def test_unique_paths(m: int, n: int, expected: int) -> None:
    assert unique_paths(m, n) == expected
