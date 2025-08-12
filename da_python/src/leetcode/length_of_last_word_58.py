"""
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=nuqdjkwd

[Problem Description]
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


def length_of_last_word(s: str) -> int:
    return way2(s)


def way1(s: str) -> int:
    return len(s.split()[-1])


def way2(s: str) -> int:
    e_idx = len(s) - 1

    while s[e_idx] == " ":
        e_idx -= 1

    s_idx = e_idx
    while s[s_idx] != " " and s_idx >= 0:
        s_idx -= 1

    return e_idx - s_idx
