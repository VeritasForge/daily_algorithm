from collections import Counter, defaultdict


# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
#
# Example 1:
#   Input: s = "anagram", t = "nagaram"
#   Output: true
#
# Example 2:
#   Input: s = "rat", t = "car"
#   Output: false
#
# Constraints:
#   - 1 <= s.length, t.length <= 5 * 10^4
#   - s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain unicode characters?
#            How would you adapt your solution to such case?


def is_anagram(s: str, t: str) -> bool:
    # return pythonic_way(s, t)
    # return using_default_dict(s, t)
    # return using_default_dict2(s, t)
    # return using_zip(s, t)
    return using_sorting(s, t)


def pythonic_way(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def using_default_dict(s: str, t: str) -> bool:
    count_s: dict[str, int] = defaultdict(int)
    count_t: dict[str, int] = defaultdict(int)

    for c in s:
        count_s[c] += 1

    for c in t:
        count_t[c] += 1

    return count_s == count_t


def using_default_dict2(s: str, t: str) -> bool:
    counter: dict[str, int] = defaultdict(int)

    for c in s:
        counter[c] += 1

    for c in t:
        counter[c] -= 1

    return all(n == 0 for n in counter.values())


def using_zip(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter: dict[str, int] = defaultdict(int)
    for cs, ct in zip(s, t):
        counter[cs] += 1
        counter[ct] -= 1

    return all(n == 0 for n in counter.values())


def using_sorting(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
