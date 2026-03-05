"""
342. Power of Four
https://leetcode.com/problems/power-of-four/

Difficulty: Easy

문제 설명:
    정수 n이 주어졌을 때, 4의 거듭제곱이면 true를, 아니면 false를 반환하라.
    정수 n이 4의 거듭제곱이란, n == 4^x를 만족하는 정수 x가 존재하는 것이다.

제약 조건:
    -2^31 <= n <= 2^31 - 1

Follow up:
    반복문/재귀 없이 풀 수 있는가?
"""

# def is_power_of_four(n: int) -> bool:
#     return n > 0 and n & (n - 1) == 0 and n % 3 == 1


def is_power_of_four(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0


# def is_power_of_four(n: int) -> bool:
#     if n <= 0:
#         return False
#
#     curr = 1
#     while curr < n:
#         curr *= 4
#
#     return curr == n

# def is_power_of_four(n: int) -> bool:
#     if n <= 0:
#         return False
#
#     while n % 4 == 0:
#         n //= 4
#
#     return n == 1

# def is_power_of_four(n: int) -> bool:
#     if n <= 0:
#         return False
#
#     def f(curr = 1):
#         if curr == n:
#             return True
#
#         if curr > n:
#             return False
#
#         return f(curr * 4)
#
#     return f()
