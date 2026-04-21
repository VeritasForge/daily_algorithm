"""
Tests for frequency_of_string.py

인코딩 규칙별 시나리오와 엣지 케이스를 검증한다.
"""

import pytest

from src.etc.frequency_of_string import solution


def freq(*pairs: tuple[str, int]) -> list[int]:
    """헬퍼: ('a', 2), ('b', 3) 형태로 주면 26칸 배열을 만들어준다."""
    result = [0] * 26
    for char, count in pairs:
        result[ord(char) - ord("a")] = count
    return result


# -- 원문 샘플 케이스 --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 샘플 0: "abzx"
        ("1226#24#", freq(("a", 1), ("b", 1), ("z", 1), ("x", 1))),
        # 샘플 1: "aabbccc"
        ("1(2)23(3)", freq(("a", 2), ("b", 1), ("c", 3))),
        # 샘플 2: "bajj"
        ("2110#(2)", freq(("b", 1), ("a", 1), ("j", 2))),
        # 샘플 3: "wwxyzwww"
        ("23#(2)24#25#26#23#(3)", freq(("w", 5), ("x", 1), ("y", 1), ("z", 1))),
    ],
)
def test_sample_cases(s: str, expected: list[int]):
    assert solution(s) == expected


# -- 한 자리 숫자 (a-i) --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 'abc' → a=1, b=1, c=1
        ("123", freq(("a", 1), ("b", 1), ("c", 1))),
        # 'aaa' → a=3
        ("1(3)", freq(("a", 3))),
        # 'aabbb' → a=2, b=3
        ("1(2)2(3)", freq(("a", 2), ("b", 3))),
        # 'i' → i=1
        ("9", freq(("i", 1))),
    ],
)
def test_single_digit(s: str, expected: list[int]):
    assert solution(s) == expected


# -- 두 자리 숫자 + # (j-z) --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 'j' → j=1
        ("10#", freq(("j", 1))),
        # 'jkk' → j=1, k=2
        ("10#11#(2)", freq(("j", 1), ("k", 2))),
        # 'z' → z=1
        ("26#", freq(("z", 1))),
        # 'zzz' → z=3
        ("26#(3)", freq(("z", 3))),
    ],
)
def test_double_digit_with_hash(s: str, expected: list[int]):
    assert solution(s) == expected


# -- 한 자리 + 두 자리 혼합 --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 'ajk' → a=1, j=1, k=1 (110#11# → 1, 10#, 11#)
        ("110#11#", freq(("a", 1), ("j", 1), ("k", 1))),
        # 'aajjbb' → a=2, j=2, b=2
        ("1(2)10#(2)2(2)", freq(("a", 2), ("j", 2), ("b", 2))),
        # 'abcij' → a=1,b=1,c=1,i=1,j=1 (12310#가 아니라 1239 10#으로 파싱)
        ("12910#", freq(("a", 1), ("b", 1), ("i", 1), ("j", 1))),
    ],
)
def test_mixed_single_and_double(s: str, expected: list[int]):
    assert solution(s) == expected


# -- 큰 반복 횟수 --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 'a' * 100 → a=100
        ("1(100)", freq(("a", 100))),
        # 'z' * 500 → z=500
        ("26#(500)", freq(("z", 500))),
        # 'w' * 10000 (c 최대값) → w=10000
        ("23#(10000)", freq(("w", 10000))),
    ],
)
def test_large_repeat_count(s: str, expected: list[int]):
    assert solution(s) == expected


# -- 반복 없는 연속 한 자리 숫자 --


@pytest.mark.parametrize(
    "s, expected",
    [
        # 'abcdefghi' → 각 1개
        (
            "123456789",
            freq(
                ("a", 1),
                ("b", 1),
                ("c", 1),
                ("d", 1),
                ("e", 1),
                ("f", 1),
                ("g", 1),
                ("h", 1),
                ("i", 1),
            ),
        ),
    ],
)
def test_all_single_digits(s: str, expected: list[int]):
    assert solution(s) == expected
