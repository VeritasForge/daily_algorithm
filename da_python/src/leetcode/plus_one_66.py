"""
URL: https://leetcode.com/problems/plus-one/
Title: 66. Plus One
Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


def plus_one(digits: list[int]) -> list[int]:
    """
    Increments the large integer by one and returns the resulting array of digits.
    """
    return way2(digits)


def way1(digits: list[int]):
    num = 0
    for i, v in enumerate(digits):
        num += 10 ** (len(digits) - 1 - i) * v
    num += 1

    l_idx = len(digits) if all(d == 9 for d in digits) else len(digits) - 1
    result = []

    for i in range(l_idx, -1, -1):
        divisor = 10**i
        quotient = num // divisor
        result.append(quotient)
        num -= divisor * quotient

    return result


def way2(digits: list[int]):
    for i in range(len(digits) - 1, -1, -1):
        result = digits[i] + 1
        if result < 10:
            digits[i] = result
            return digits

        digits[i] = 0

    return [1] + digits
