"""
1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Difficulty: Easy

문제 설명:
    숫자와 '#'으로 구성된 문자열 s가 주어진다.
    s를 영어 소문자로 매핑하려 한다:

    - 'a' ~ 'i'는 '1' ~ '9'로 표현된다.
    - 'j' ~ 'z'는 '10#' ~ '26#'로 표현된다.

    매핑 후 형성된 문자열을 반환하라.
    테스트 케이스는 항상 유일한 매핑이 존재하도록 생성된다.

제약 조건:
    - 1 <= s.length <= 1000
    - s는 숫자와 '#' 문자로만 구성
    - s는 항상 유효한 매핑이 가능한 문자열
"""


def freq_alphabets(s: str) -> str:
    i, res = 0, []

    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == "#":
            res.append(chr(int(s[i : i + 2]) + ord("a") - 1))
            i += 3
        else:
            res.append(chr(int(s[i]) + ord("a") - 1))
            i += 1

    return "".join(res)


# import string

# def freq_alphabets(s: str) -> str:
#     i, res = 0, []
#
#     while i < len(s):
#         if i + 2 < len(s) and s[i + 2] == "#":
#             ch_idx = s[i : i + 2]
#             i += 3
#         else:
#             ch_idx = s[i]
#             i += 1
#
#         res.append(string.ascii_lowercase[int(ch_idx) - 1])
#
#     return "".join(res)


# def freq_alphabets(s: str) -> str:
#     i, res = len(s) - 1, []
#
#     while i >= 0:
#         if s[i] == "#":
#             ch_idx = int(s[i - 2 : i])
#             i -= 3
#         else:
#             ch_idx = int(s[i])
#             i -= 1
#
#         res.append(string.ascii_lowercase[ch_idx - 1])
#
#     return "".join(res[::-1])


# def freq_alphabets(s: str) -> str:
#     for i in range(26, 0, -1):
#         s = s.replace(str(i) + ("#" * (i > 9)), chr(96 + i))
#     return s
