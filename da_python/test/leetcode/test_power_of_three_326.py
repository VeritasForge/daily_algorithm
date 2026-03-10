import pytest

from src.leetcode.power_of_three_326 import is_power_of_three


@pytest.mark.parametrize(
    "n, expected",
    [
        # 기본 예제
        (27, True),
        (0, False),
        (-1, False),
        # 3의 거듭제곱
        (1, True),  # 3^0
        (3, True),  # 3^1
        (9, True),  # 3^2
        (243, True),  # 3^5
        # 3의 거듭제곱이 아닌 수
        (2, False),
        (4, False),
        (6, False),  # 3의 배수이지만 거듭제곱 아님
        (45, False),  # 3^2 * 5
        (10, False),
        # 엣지 케이스
        (-3, False),  # 음수
        (-27, False),  # 음수 거듭제곱
        # 큰 수
        (1162261467, True),  # 3^19 (int 범위 내 최대 3의 거듭제곱)
        (1162261468, False),  # 3^19 + 1
    ],
)
def test_is_power_of_three(n: int, expected: bool) -> None:
    assert is_power_of_three(n) == expected
