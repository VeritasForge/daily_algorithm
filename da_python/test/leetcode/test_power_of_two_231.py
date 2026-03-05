import pytest

from src.leetcode.power_of_two_231 import is_power_of_two


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),  # 2^0
        (2, True),  # 2^1
        (4, True),  # 2^2
        (16, True),  # 2^4
        (1024, True),  # 2^10
        (2**30, True),  # 2^30 (최대 2의 거듭제곱)
        (0, False),  # 0은 2의 거듭제곱이 아님
        (-1, False),  # 음수
        (-16, False),  # 음수 (절댓값은 2의 거듭제곱)
        (3, False),  # 일반 홀수
        (6, False),  # 일반 짝수
        (5, False),  # 2의 거듭제곱 사이 값
        (2**31 - 1, False),  # int 최댓값
    ],
)
def test_is_power_of_two(n: int, expected: bool):
    assert is_power_of_two(n) == expected
