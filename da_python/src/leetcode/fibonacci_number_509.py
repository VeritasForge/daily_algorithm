"""
URL: https://leetcode.com/problems/fibonacci-number/description/
Title: 509. Fibonacci Number
---
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30
"""


def fib(n: int) -> int:
    return way4(n)


# 시간 복잡도 : O(2^n)
# 공간 복잡도 : O(n)
def way1(n: int) -> int:
    if n <= 1:
        return n

    return way1(n - 2) + way1(n - 1)


# 시간 복잡도 : O(n)
# 공간 복잡도 : O(n)
memo = {0: 0, 1: 1}


def way2(n: int) -> int:
    if n in memo:
        return memo[n]

    memo[n] = way2(n - 2) + way2(n - 1)
    return memo[n]


# Tabulation
# 시간 복잡도 : O(n)
# 공간 복잡도 : O(n)
def way3(n: int) -> int:
    if n <= 1:
        return n

    res = [0, 1]
    for i in range(1, n):
        res.append(res[i] + res[i - 1])
    return res[-1]


# 시간 복잡도 : O(n)
# 공간 복잡도 : O(1)
def way4(n: int) -> int:
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(1, n):
        prev, curr = curr, prev + curr
    return curr
