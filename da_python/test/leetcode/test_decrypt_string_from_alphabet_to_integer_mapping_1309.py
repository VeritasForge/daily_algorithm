import pytest

from src.leetcode.decrypt_string_from_alphabet_to_integer_mapping_1309 import (
    freq_alphabets,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        # LeetCode 기본 예제
        # "10#" → j, "11#" → k, "1" → a, "2" → b
        ("10#11#12", "jkab"),
        # "1" → a, "3" → c, "26#" → z
        ("1326#", "acz"),
        # 보강 - 한 자리 숫자만
        ("123456789", "abcdefghi"),
        # 보강 - 두 자리 + # 만
        ("10#11#12#13#", "jklm"),
        # 보강 - 단일 문자
        ("1", "a"),
        ("9", "i"),
        ("10#", "j"),
        ("26#", "z"),
        # 보강 - 혼합 (한 자리 사이에 두 자리)
        ("110#11#2", "ajkb"),
        # 보강 - 연속 두 자리
        ("25#26#", "yz"),
        # 보강 - 모든 두 자리 경계값
        ("10#26#", "jz"),
    ],
)
def test_freq_alphabets(s: str, expected: str):
    assert freq_alphabets(s) == expected
