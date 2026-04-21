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
    위치 j의 문자 c에 대해, 이전에 c가 나온 가장 최근 위치 l을 추적한다.
    후보 구간 [l, j]는 j를 오른쪽 끝으로 하는 가장 짧은 c 구간이다.
    이전 선택 구간과 겹치지 않으면 탐욕적으로 선택한다.

    탐욕법 교환 논증:
        더 긴 구간을 선택한 최적해가 있다면, 항상 더 짧은 구간으로 교체
        가능하고 개수는 줄지 않는다. 따라서 가장 짧은 구간 우선 선택이 최적.
"""


def solution(S: str) -> int:
    visits, last_visit = {}, -1
    res = 0

    for i, c in enumerate(S):
        if c in visits and last_visit < visits[c]:
            last_visit = i
            res += 1

        visits[c] = i

    return res


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
