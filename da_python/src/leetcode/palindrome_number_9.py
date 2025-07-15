"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while reverted_number < x:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10

    return reverted_number == x or x == reverted_number // 10


def _way_1(x: int) -> bool:
    if x < 0:
        return False

    reverted_number = 0
    tmp = x
    while tmp:
        reverted_number = reverted_number * 10 + tmp % 10
        tmp //= 10

    return reverted_number == x


def _way_2(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10

    return x == reverted_number or x == reverted_number // 10
