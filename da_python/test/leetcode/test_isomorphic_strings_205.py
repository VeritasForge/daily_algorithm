import pytest

from src.leetcode.isomorphic_strings_205 import is_isomorphic


@pytest.mark.parametrize(
    "s, t, expected",
    [
        # LeetCode 기본 예제
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        # 보강 - 엣지 케이스
        ("a", "a", True),
        ("a", "b", True),
        ("abc", "abc", True),
        # 보강 - 예외 케이스 (다대일/일대다 매핑 위반)
        ("ab", "aa", False),
        ("aa", "ab", False),
        ("badc", "baba", False),
        # 보강 - 추가 검증 (양방향 매핑 확인이 필요한 케이스)
        ("bbbaaaba", "aaabbbba", False),
    ],
)
def test_is_isomorphic(s: str, t: str, expected: bool):
    assert is_isomorphic(s, t) == expected
