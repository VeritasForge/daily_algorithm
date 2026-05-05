import pytest

from src.leetcode.counting_bits_338 import count_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        # LeetCode 기본 예제
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        # 보강 - 엣지 케이스 (제약 조건 최솟값)
        (0, [0]),
        (1, [0, 1]),
        # 보강 - 2의 거듭제곱 경계 (비트 패턴이 1로 리셋되는 지점)
        (4, [0, 1, 1, 2, 1]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
        # 보강 - 일반적인 케이스 (모든 비트가 1인 값 포함, 7 = 111)
        (7, [0, 1, 1, 2, 1, 2, 2, 3]),
        # 보강 - 더 넓은 범위 (16 = 10000, 비트 1개로 리셋)
        (
            16,
            [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1],
        ),
    ],
)
def test_count_bits(n: int, expected: list[int]) -> None:
    assert count_bits(n) == expected
