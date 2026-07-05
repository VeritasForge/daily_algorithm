import pytest

from src.leetcode.pascals_triangle_118 import generate


@pytest.mark.parametrize(
    "num_rows, expected",
    [
        # LeetCode 기본 예제
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        # 보강 - 엣지 케이스 (최솟값 경계)
        (2, [[1], [1, 1]]),
        # 보강 - 추가 검증 (각 행의 대칭성)
        (3, [[1], [1, 1], [1, 2, 1]]),
    ],
)
def test_generate(num_rows: int, expected: list[list[int]]):
    assert generate(num_rows) == expected


def test_generate_max_num_rows_length():
    result = generate(30)
    assert len(result) == 30
    assert result[-1][0] == 1
    assert result[-1][-1] == 1
