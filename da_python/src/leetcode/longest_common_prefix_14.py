"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


def longest_common_prefix(strs):
    min_s = min(strs, key=lambda x: len(x))

    for i, s in enumerate(strs):
        if min_s == s:
            continue

        common_prefix = []
        for i, c in enumerate(min_s):
            if s[i] != c:
                break

            common_prefix.append(c)

        min_s = "".join(common_prefix)

    return min_s
