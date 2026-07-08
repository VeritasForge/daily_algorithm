import pytest

from src.leetcode.excel_sheet_column_title_168 import convert_to_title


@pytest.mark.parametrize(
    "column_number, expected",
    [
        # LeetCode 기본 예제
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
        # 보강 - 엣지 케이스 (26의 배수 경계값)
        (26, "Z"),
        (27, "AA"),
        (52, "AZ"),
        (53, "BA"),
        (702, "ZZ"),
        (703, "AAA"),
        # 보강 - 최댓값 (2^31 - 1)
        (2147483647, "FXSHRXW"),
    ],
)
def test_convert_to_title(column_number: int, expected: str):
    assert convert_to_title(column_number) == expected
