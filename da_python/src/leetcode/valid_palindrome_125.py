# https://leetcode.com/problems/valid-palindrome/description/
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
# Constraints:
#
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


import re


# pythonic way
def is_palindrome(s: str) -> bool:
    # return _pythonic(s)
    return _using_two_point(s)


def _pythonic(s: str) -> bool:
    filtered_str = "".join(c for c in s.lower() if c.isalnum())
    return filtered_str == filtered_str[::-1]


def _using_two_point(s: str) -> bool:
    # filtered_str = "".join(c for c in s.lower() if c.isalnum())
    filtered_str = re.sub("[^0-9a-zA-Z]", "", s).lower()
    left, right = 0, len(filtered_str) - 1

    # for _ in range(len(filtered_str) // 2):
    while left < right:
        if filtered_str[left] != filtered_str[right]:
            return False

        left += 1
        right -= 1

    return True
