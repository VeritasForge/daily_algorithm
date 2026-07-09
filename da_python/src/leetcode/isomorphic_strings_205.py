"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Difficulty: Easy

문제 설명:
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be
    replaced to get t.

    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to
    the same character, but a character may map to itself.

    Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Explanation:
        Mapping 'e' to 'a'.
        Mapping 'g' to 'd'.

    Example 2:

    Input: s = "f11", t = "b23"
    Output: false
    Explanation:
        's' and 't' can not be made identical as '1' needs to be mapped to
        both '2' and '3'.

    Example 3:

    Input: s = "paper", t = "title"
    Output: true

제약 조건:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
"""


# def is_isomorphic(s: str, t: str) -> bool:
#     s_to_t, t_to_s = {}, {}
#     for s_c, t_c in zip(s, t):
#         if s_to_t.setdefault(s_c, t_c) != t_c or t_to_s.setdefault(t_c, s_c) != s_c:
#             return False
#     return True


def is_isomorphic(s: str, t: str) -> bool:
    s_to_t, t_to_s = {}, {}
    return all(s_to_t.setdefault(s_c, t_c) == t_c and t_to_s.setdefault(t_c, s_c) == s_c for s_c, t_c in zip(s, t))
