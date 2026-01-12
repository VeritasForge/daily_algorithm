"""
https://leetcode.com/problems/longest-palindrome

409. Longest Palindrome (Easy)

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd",
    whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1

Example 3:
    Input: s = "bb"
    Output: 2

Constraints:
    - 1 <= s.length <= 2000
    - s consists of lowercase and/or uppercase English letters only.
"""


# def longest_palindrome(s: str) -> int:
#     counter = Counter(s)
#     odd, length = 0, 0
#
#     for v in counter.values():
#         mod = v % 2
#         length += v - mod
#         if mod:
#             odd = 1
#
#     return length + odd


# def longest_palindrome(s: str) -> int:
#     counter = Counter(s)
#     odd_count = sum(v % 2 for v in counter.values())
#     return len(s) - odd_count + (1 if odd_count else 0)


def longest_palindrome(s: str) -> int:
    seen = set()
    for c in s:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)

    return len(s) - len(seen) + (1 if seen else 0)
