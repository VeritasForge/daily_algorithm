import pytest

from src.leetcode.power_of_four_342 import is_power_of_four


@pytest.mark.parametrize(
    "n, expected",
    [
        # 기본 예제
        (16, True),
        (5, False),
        (1, True),
        # 4의 거듭제곱
        (4, True),
        (64, True),
        (256, True),
        (1073741824, True),  # 4^15 = 2^30, 제약 범위 내 최대
        # 4의 거듭제곱이 아닌 2의 거듭제곱 (함정)
        (2, False),
        (8, False),
        (32, False),
        # 엣지 케이스
        (0, False),
        (-1, False),
        (-4, False),
        (-2147483648, False),  # -2^31
        # 4의 거듭제곱에 가까운 값
        (3, False),
        (15, False),
        (17, False),
        (65, False),
    ],
)
def test_is_power_of_four(n: int, expected: bool):
    assert is_power_of_four(n) == expected
