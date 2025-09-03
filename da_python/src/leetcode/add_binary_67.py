"""
URL: https://leetcode.com/problems/add-binary/
Title: 67. Add Binary
---
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def add_binary(a: str, b: str) -> str:
    return way3(a, b)


def way1(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def way2(a: str, b: str) -> str:
    a_idx, b_idx = len(a) - 1, len(b) - 1

    stack = []
    inc = 0
    for _ in range(max(len(a), len(b))):
        a_val = b_val = 0

        if a_idx >= 0:
            a_val = int(a[a_idx])
            a_idx -= 1

        if b_idx >= 0:
            b_val = int(b[b_idx])
            b_idx -= 1

        match a_val + b_val + inc:
            case 0:
                stack.append(0)
                inc = 0
            case 1:
                stack.append(1)
                inc = 0
            case 2:
                stack.append(0)
                inc = 1
            case 3:
                stack.append(1)
                inc = 1

    if inc == 1:
        stack.append(1)

    return "".join(str(stack[i]) for i in range(len(stack) - 1, -1, -1))


def way3(a: str, b: str) -> str:
    carry = 0
    res = []

    a_idx, b_idx = len(a) - 1, len(b) - 1

    while a_idx >= 0 or b_idx >= 0 or carry:
        if a_idx >= 0:
            carry += int(a[a_idx])
            a_idx -= 1
        if b_idx >= 0:
            carry += int(b[b_idx])
            b_idx -= 1

        res.append(str(carry % 2))
        carry = carry // 2

    return "".join(res[::-1])
