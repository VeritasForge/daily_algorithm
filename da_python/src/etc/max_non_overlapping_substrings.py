"""
Maximum Non-Overlapping Substrings
(Codility-style problem)

문제 원문 (English):
    You are given a string S consisting of lowercase English letters only.
    A substring is defined as a contiguous segment of a string. For example,
    "dad", "daddy", "d" and "dd" are substrings of "daddy", but "dady" is not.

    Your task is to find the maximum number of non-overlapping substrings
    such that each substring:
      - starts and ends with the same character
      - contains at least two characters

    The characters at the beginning and end of each substring must be identical,
    but different substrings can start and end with different characters.

    Given a string S of length N, return the maximum number of substrings that
    can be selected from S while satisfying the described conditions.

    Examples:
      S = "sashalikesana" → 2
        [sas]h[alikesana], [sas]h[alikesa]na, sa[shalikes][ana] are all valid.

      S = "zzaaabbccall" → 5
        [zz][aaa][bb][cc]a[ll]

      S = "thing" → 0
        No substring of length ≥ 2 starts and ends with the same character.

    Constraints:
      - N is an integer within the range [1, 200,000]
      - S consists only of lowercase letters (a-z)

문제 원문 (Korean):
    You are given a string S consisting of lowercase English letters only.
    A substring is defined as a contiguous segment of a string. For example,
    "dad", "daddy", "d" and "dd" are substrings of "daddy", but "dady" is not.

    Your task is to find the maximum number of non-overlapping substrings
    such that each substring starts and ends with the same character and
    contains at least two characters. The characters at the beginning and
    end of each substring must be identical, but different substrings can
    start and end with different characters.

    For example, for the string "sashalikesana":
      - [sas]h[alikesana]  → valid (2 substrings)
      - [sas]h[alikesa]na  → valid (2 substrings)
      - s[a[shalikes]ana]  → INVALID (substrings overlap)
      - sa[shalikes][ana]  → valid (2 substrings)

문제 설명:
    영어 소문자로만 구성된 문자열이 주어질 때,
    각각 동일한 문자로 시작하고 끝나며 최소 두 개의 문자를 포함하는
    교차하지 않는 하위 문자열의 최대 개수를 구한다.

입력:
    S: str - 영어 소문자로만 구성된 문자열

출력:
    int - 조건을 만족하는 교차하지 않는 하위 문자열의 최대 개수

제약 조건:
    - N (문자열 길이): 1 ≤ N ≤ 200,000
    - S는 영어 소문자(a-z)로만 구성

핵심 아이디어 (O(n) 탐욕법):
    지금까지 본 문자들을 set으로 추적하며 문자열을 순회한다.
    현재 문자가 set에 이미 있으면 유효한 구간(같은 문자로 시작·끝)을
    발견한 것이므로, 카운트를 증가시키고 set을 비워 다음 구간을 탐색한다.

    set.clear()는 "이전 구간 이후의 문자만 추적"하는 효과를 만들어,
    별도의 위치 추적 없이 겹침 방지를 보장한다.

    탐욕법 교환 논증:
        반복 문자를 발견하는 즉시 매칭하므로 항상 가장 짧은 구간을 선택한다.
        더 긴 구간을 선택한 최적해가 있다면, 짧은 구간으로 교체해도
        개수는 줄지 않고 남은 공간이 넓어진다. 따라서 최적.

    적용 패턴:
        - "겹치지 않는 최대 개수" → 탐욕법 후보
        - "가장 짧은/빠른 것 우선" → 교환 논증으로 최적성 증명
        - 위치 추적이 필요해 보여도, set + clear로 단순화 가능한지 점검
"""


def solution(S: str) -> int:
    """동일한 문자로 시작하고 끝나는 교차하지 않는 하위 문자열의 최대 개수를 반환한다.

    Args:
        S: 영어 소문자로만 구성된 문자열

    Returns:
        조건을 만족하는 교차하지 않는 하위 문자열의 최대 개수

    Examples:
        >>> solution("sashalikesana")
        2
        >>> solution("zzaaabbccall")
        5
        >>> solution("thing")
        0
    """
    visits = set()
    res = 0

    for c in S:
        if c in visits:
            res += 1
            visits.clear()
        else:
            visits.add(c)

    return res


# def solution(S: str) -> int:
#     visits, last_visit = {}, -1
#     res = 0
#
#     for i, c in enumerate(S):
#         if c in visits and last_visit < visits[c]:
#             last_visit = i
#             res += 1
#
#         visits[c] = i
#
#     return res


# def solution(S: str) -> int:
#     """
#     동일한 문자로 시작하고 끝나는 교차하지 않는 하위 문자열의 최대 개수를 반환한다.
#
#     Args:
#         S: 영어 소문자로만 구성된 문자열
#
#     Returns:
#         조건을 만족하는 교차하지 않는 하위 문자열의 최대 개수
#
#     Examples:
#         >>> solution("sashalikesana")
#         2
#         >>> solution("zzaaabbccall")
#         5
#         >>> solution("thing")
#         0
#     """
#     last_seen: dict[str, int] = {}  # 각 문자의 가장 최근 위치
#     count = 0
#     last_end = -1  # 마지막으로 선택한 구간의 오른쪽 끝
#
#     for j, c in enumerate(S):
#         if c in last_seen:
#             l = last_seen[c]
#             # [l, j]가 이전 선택 구간과 겹치지 않으면 선택
#             if l > last_end:
#                 count += 1
#                 last_end = j
#         last_seen[c] = j
#
#     return count
