import pytest

from src.leetcode.excel_sheet_column_number_171 import title_to_number


@pytest.mark.parametrize(
    "column_title, expected",
    [
        # LeetCode 기본 예제
        ("A", 1),
        ("AB", 28),
        ("ZY", 701),
        # 보강 - 엣지 케이스 (26의 배수 경계값)
        ("Z", 26),
        ("AA", 27),
        ("AZ", 52),
        ("BA", 53),
        ("ZZ", 702),
        ("AAA", 703),
        # 보강 - 최댓값 길이 (7자, 문제 범위의 최댓값)
        ("FXSHRXW", 2147483647),
    ],
)
def test_title_to_number(column_title: str, expected: int):
    assert title_to_number(column_title) == expected
