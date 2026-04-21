"""
Tests for max_non_overlapping_substrings.py

문제에서 주어진 예시, 경계값, 탐욕법 최적성을 독립적으로 검증한다.
"""

import pytest

from src.etc.max_non_overlapping_substrings import solution


# ── 문제에서 주어진 예시 ───────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "S, expected",
    [
        # [sas]h[alikesana] 또는 sa[shalikes][ana] 등 → 2
        ("sashalikesana", 2),
        # [zz][aaa][bb][cc]a[ll] → 5
        ("zzaaabbccall", 5),
        # 동일한 문자로 시작/끝나는 길이 2 이상 하위 문자열 없음 → 0
        ("thing", 0),
    ],
)
def test_given_examples(S: str, expected: int):
    assert solution(S) == expected


# ── 경계값 및 엣지 케이스 ─────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "S, expected",
    [
        # 단일 문자: 쌍을 이룰 수 없음
        ("a", 0),
        # 동일한 두 문자: 하나의 구간
        ("aa", 1),
        # 서로 다른 두 문자: 구간 없음
        ("ab", 0),
        # 모든 문자가 유일: 구간 없음
        ("abcdefghijklmnopqrstuvwxyz", 0),
        # 동일 문자 4개: [aa][aa] → 2
        ("aaaa", 2),
        # 동일 문자 6개: [aa][aa][aa] → 3
        ("aaaaaa", 3),
        # 동일 문자 홀수개: [aa][aa]a → 2
        ("aaaaa", 2),
    ],
)
def test_edge_cases(S: str, expected: int):
    assert solution(S) == expected


# ── 탐욕법 최적성 검증 ────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "S, expected",
    [
        # 인접 쌍: [aa][bb][cc] → 3
        ("aabbcc", 3),
        # 중첩 구조: [bb] 또는 [abba] 각각 1, 최대 1
        ("abba", 1),
        # 짧은 구간 우선: [a(0,2)] + [a(4,6)] = 2
        # "abacaba": a=[0,2,4,6], b=[1,5], c=[3]
        ("abacaba", 2),
        # 교차 문자: [a(0,2)] + [b(3,5)] = 2
        # "ababab": a=[0,2,4], b=[1,3,5]
        ("ababab", 2),
        # 긴 간격 내부: 내부 [cc][cc][cc] = 3 이 [acccccca] = 1 보다 이득
        ("acccccca", 3),
        # 인접 두 종류: [aa][bb] → 2
        ("aabb", 2),
        # 단일 반복: [aba] → 1
        ("aba", 1),
    ],
)
def test_greedy_optimality(S: str, expected: int):
    assert solution(S) == expected


# ── last_seen 업데이트로 나중에 구간 선택 가능 ────────────────────────────────


@pytest.mark.parametrize(
    "S, expected",
    [
        # "aaba": j=1 [0,1] 선택, j=3 [1,3] 1>1 불가 → 1
        ("aaba", 1),
        # "abcabc": j=3 [a:0,3] 선택, j=4 [b:1,4] 1>3 불가, j=5 [c:2,5] 2>3 불가 → 1
        ("abcabc", 1),
        # "xaaxbbx": [aa][bb] → 2
        ("xaaxbbx", 2),
        # "xaax": [aa](1,2) 선택 → 1
        ("xaax", 1),
        # "ababababab": a=[0,2,4,6,8], b=[1,3,5,7,9]
        # 탐욕: [a(0,2)] + [b(3,5)] + [a(6,8)] → 3? 확인
        # j=2 a(0,2) pick(end=2), j=3 b(1,3) 1>2? No, j=4 a(2,4) 2>2? No,
        # j=5 b(3,5) 3>2 Yes pick(end=5), j=6 a(4,6) 4>5? No,
        # j=7 b(5,7) 5>5? No, j=8 a(6,8) 6>5 Yes pick(end=8), j=9 b(7,9) 7>8? No
        # → 3
        ("ababababab", 3),
    ],
)
def test_last_seen_update(S: str, expected: int):
    assert solution(S) == expected


# ── 대용량 입력 성능 테스트 ───────────────────────────────────────────────────


def test_large_input_all_same():
    """N=200,000 동일 문자: 100,000쌍 선택."""
    n = 200_000
    assert solution("a" * n) == n // 2


def test_large_input_alternating():
    """N=200,000 두 문자 교대: O(n) 내 처리."""
    n = 200_000
    s = "ab" * (n // 2)
    result = solution(s)
    assert result > 0


def test_large_input_all_unique_pattern():
    """N=200,000 26자 반복: O(n) 내 처리."""
    import string

    n = 200_000
    s = (string.ascii_lowercase * (n // 26 + 1))[:n]
    result = solution(s)
    assert result > 0
