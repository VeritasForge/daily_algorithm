import pytest

from src.leetcode.pascals_triangle_ii_119 import get_row


@pytest.mark.parametrize(
    "row_index, expected",
    [
        # LeetCode 기본 예제
        (3, [1, 3, 3, 1]),
        (0, [1]),
        (1, [1, 1]),
        # 보강 - 엣지 케이스 (최솟값 경계)
        (2, [1, 2, 1]),
        # 보강 - 추가 검증 (대칭성 확인)
        (4, [1, 4, 6, 4, 1]),
    ],
)
def test_get_row(row_index: int, expected: list[int]):
    assert get_row(row_index) == expected


def test_get_row_max_row_index():
    result = get_row(33)
    assert len(result) == 34
    assert result[0] == 1
    assert result[-1] == 1
    assert result == result[::-1]
