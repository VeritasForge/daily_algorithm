import pytest

from src.leetcode.number_of_1_bits_191 import hamming_weight


@pytest.mark.parametrize(
    "n, expected",
    [
        # LeetCode 기본 예제
        (11, 3),  # 1011
        (128, 1),  # 10000000
        (2147483645, 30),  # 1111111111111111111111111111101
        # 보강 - 엣지 케이스 (제약 조건 경계)
        (1, 1),  # 최솟값: 1 (binary: 1)
        (2147483647, 31),  # 최댓값: 2^31 - 1, 모든 31비트가 1
        # 보강 - 2의 거듭제곱 (set bit가 정확히 1개)
        (2, 1),  # 10
        (4, 1),  # 100
        (1024, 1),  # 2^10
        (1073741824, 1),  # 2^30
        # 보강 - 모든 비트가 1인 패턴 (2^k - 1)
        (3, 2),  # 11
        (7, 3),  # 111
        (15, 4),  # 1111
        (255, 8),  # 11111111
        # 보강 - 교차 패턴 / 일반 케이스
        (5, 2),  # 101
        (10, 2),  # 1010
        (170, 4),  # 10101010
    ],
)
def test_hamming_weight(n: int, expected: int) -> None:
    assert hamming_weight(n) == expected
