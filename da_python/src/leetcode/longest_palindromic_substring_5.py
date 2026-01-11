"""
https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring (Medium)

Given a string s, return the longest palindromic substring in s.

A string is palindromic if it reads the same forward and backward.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    - 1 <= s.length <= 1000
    - s consist of only digits and English letters.
"""


def longest_palindrome(s: str) -> str:
    def _expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    result = ""
    for i, _ in enumerate(s):
        result = max(result, _expand(s, i, i), _expand(s, i, i + 1), key=len)
    return result
